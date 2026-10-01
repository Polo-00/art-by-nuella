/**
 * Art by Nuella — quote form backend (Google Sheets + email notification)
 *
 * Paste this whole file into Extensions > Apps Script inside a Google Sheet.
 * Every form submission from the website becomes a new row, and an email is sent to NOTIFY_EMAIL.
 * Setup steps are in README-forms.md.
 */
const NOTIFY_EMAIL = 'artbynuella@gmail.com';   // who gets the "new request" email
const SHEET_NAME = 'Requests';                   // the tab the rows are saved to (created automatically)

function doPost(e) {
  const p = (e && e.parameter) || {};

  // Ignore obvious junk (the form also has a hidden honeypot field for bots).
  if (p.website || (!p.name && !p.contact)) return json_({ ok: true });

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) {
    sh = ss.insertSheet(SHEET_NAME);
    sh.appendRow(['Received', 'Name', 'Phone or email', 'City', 'Timeline / event date', 'Project type', 'Details', 'Page', 'Status']);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, 9).setFontWeight('bold').setBackground('#f3e2c4');
    sh.setColumnWidth(7, 420);
  }

  sh.appendRow([
    new Date(), p.name || '', p.contact || '', p.city || '', p.when || '',
    p.type || '', p.details || '', p.page || '', 'New'
  ]);

  try {
    const contact = String(p.contact || '');
    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      replyTo: contact.indexOf('@') > -1 ? contact : NOTIFY_EMAIL,
      subject: 'New quote request: ' + (p.type || 'General') + ' from ' + (p.name || 'website visitor'),
      body:
        'Name: ' + (p.name || '') + '\n' +
        'Phone or email: ' + contact + '\n' +
        'City: ' + (p.city || '') + '\n' +
        'Timeline / event date: ' + (p.when || '') + '\n' +
        'Project type: ' + (p.type || '') + '\n' +
        'Page: ' + (p.page || '') + '\n\n' +
        'Details:\n' + (p.details || '') + '\n\n' +
        'All requests are also saved in the Google Sheet.'
    });
  } catch (err) {
    // The row is already saved; an email hiccup should not lose the lead.
  }

  return json_({ ok: true });
}

// Lets you open the web app URL in a browser to check it is live.
function doGet() {
  return json_({ ok: true, service: 'Art by Nuella form backend' });
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
