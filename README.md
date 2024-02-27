![spamattacker-logo](https://github.com/reillychase/SpamAttacker/assets/17455708/462faebc-c78b-460c-b687-a7ce6247fabf)
## Our mission
End SMS spam by wasting spammers time and money. 

For more information visit https://spamattacker.com

## Build with us
We are looking for developers who are interested in contributing to this project!

[DM Reilly on X](https://x.com/_rchase_/) for more info.

## Current features

- [x] Identify the spammer's carrier and find the link to a form to submit abuse report
- [ ] Add a Telegram bot with OCR so you can just text it a screenshot of the SMS spam without having to run a Python script in a terminal
- [ ] Automate submitting the abuse forms for popular SMS providers used by spammers like Twilio
- [ ] Add support for auto-forwarding the SMS spam to the FCC at 7726 ("SPAM")
- [ ] ~~Add support for an unlimited free SMS provider so we can implement the [STOP/START attack](https://x.com/_rchase_/status/1761165629724246368?s=20)~~ Removing because it is unlikely to actually incur costs for the spammer per Tony Lewis
- [ ] Add an AI assistant (or even just if/else for MVP) to converse with the SMS spammers and try to gather more info about their identity for further reporting

## How to get started
Create a Twilio account

Copy your Account SID and Auth Token

Add this to ``` ~/.bash_profile ```
```
export TWILIO_ACCOUNT_SID="""
export TWILIO_AUTH_TOKEN="""
```


For macOS terminals also do ```echo "source ~/.bash_profile" >> ~/.zshrc```

Next download the repo
```
git clone https://github.com/reillychase/SpamAttacker.git
```
```
cd SpamAttacker
```
Install requirements
```
pip3 install twilio
```
Run the script with the spammer's number
```
python3 main.py --number "+18336585034"
```
Example output
```
The spammer's carrier is: Twilio - Toll-Free - SMS-Sybase365/MMS-SVR
You can report them here: https://www.twilio.com/en-us/help/abuse
```


