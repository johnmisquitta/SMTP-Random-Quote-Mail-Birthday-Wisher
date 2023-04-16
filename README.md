








# Random Quote Mailer

If you're looking to create new email accounts, Yahoo and Gmail are two great options. Additionally, if you're using Gmail, you may want to create an app password to use for programs that don't support two-factor authentication. In this guide, we'll walk you through the steps to create a Yahoo and Gmail account, and how to generate an app password for Gmail.

## Prerequisites

- Python 3.x
- A Gmail or Yahoo account
- Less secure apps setting enabled for Gmail
- A text file `quotes.txt` containing the quotes to be sent in the email, with one quote per line


## Creating a Yahoo Account

1. Go to the Yahoo sign-up page at [here](https://login.yahoo.com/account/create.).
2. Fill out the required information, including your first and last name, email address, password, phone number, and birth date.
3. Click "Continue" to proceed to the next step.
4. Verify your phone number by entering the verification code you receive via text message.
5. Click "Continue" to complete the sign-up process.
6. Congratulations! You've successfully created a Yahoo account.

## Creating a Gmail  Account

1. Go to the Yahoo sign-up page at [here](https://accounts.google.com/signup).
2. Fill out the required information, including your first and last name, email address, password, birth date, and gender.
3. Click "Next" to proceed to the next step.
4. Enter your phone number for account verification.
5. Google will send a verification code to your phone number. Enter the code to verify your account.
6. Congratulations! You've successfully created a Gmail account.


## Generating an App Password for Gmail

1. Go to your Google Account page at https://myaccount.google.com/.
2. Click "Security" in the left-hand menu.
3. Turn on two-factor authentication, you can generate an app password Verify your phone no. 
4. Click on two step Verification
5. Scroll down to "Signing in to Google" and click "App passwords."
6. Choose the app and device you want to generate the app password for.
7. Click "Generate" to create the app password.
8. Use the generated app password to sign in to the program or service you want to use.
9. Congratulations! You've successfully generated an app password for Gmail.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%202023-04-16%20174757.png)

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%202023-04-16%20175920.png)

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%202023-04-16%20180304.png)

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%20(53).png)

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%20(54).png)

![App Screenshot](https://raw.githubusercontent.com/johnmisquitta/SMTP-Random-Quote-Mail-Birthday-Wisher/main/Screenshots/Screenshot%20(58).png)







## Getting Started

1. Clone this repository to your local machine.

2. Open `random_quote_email.py` in your favorite code editor.

3. Replace the placeholders with your email and password information. If you're using Gmail, you may need to [allow less secure apps](https://myaccount.google.com/lesssecureapps) to access your account.

    ```python
    my_email = "your_email_address@gmail.com"
    password = "your_email_password"
    ```

4. Replace the recipient's email address with the email address you want to send the quote to.

    ```python
    to_addrs = "recipient_email_address@example.com"
    ```

5. Run the script in the terminal by navigating to the project folder and typing:

    ```sh
    $ random_quote_mail.py
    ```

The script will pick a random quote from the `quotes.txt` file, compose an email, and send it to the specified recipient.

## Customization

You can customize the quotes in the `quotes.txt` file by adding or removing quotes. Make sure each quote is on a separate line.




