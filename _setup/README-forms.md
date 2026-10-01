# Make the quote forms live (Google Sheet + email)

Takes about 5 minutes and is free. Every request lands as a row in a Google Sheet and Nuella gets an email.

1. Sign in to the Google account that should own the leads (artbynuella@gmail.com is a good choice).
2. Go to sheets.google.com and create a blank sheet named **Art by Nuella Requests**.
3. In the sheet, open **Extensions > Apps Script**.
4. Delete the sample code, paste in everything from `google-sheet-form-backend.gs`, and click **Save**.
5. Click **Deploy > New deployment**. Click the gear next to "Select type" and choose **Web app**.
   - Description: `Quote form`
   - Execute as: **Me**
   - Who has access: **Anyone**
6. Click **Deploy**. Google asks you to authorize. Choose your account, click **Advanced**, then **Go to project (unsafe)**, then **Allow**. (It says "unsafe" only because you wrote the script yourself.)
7. Copy the **Web app URL** (it starts with `https://script.google.com/macros/s/...`).
8. Open `app.js` in this folder, find `var FORM_ENDPOINT = '';` and paste the URL between the quotes.
9. Reload the site and send a test request. A new row appears in the Requests tab and an email arrives.

Notes
- If you change the script later, use **Deploy > Manage deployments > Edit > New version** so the same URL keeps working.
- Free Gmail accounts can send about 100 emails a day from a script, plenty for quote requests.
- The form has a hidden field that catches most spam bots.
- Requests are not stored on the website itself, only in your Sheet.

Other ways to do it (if you would rather not use Google)
- **Formspree or Web3Forms**: paste-in form service, emails each request. Free tiers are small (about 50 to 250 a month).
- **GoHighLevel**: the form can post into a GHL sub-account so each request becomes a contact and can trigger an automatic text back.
