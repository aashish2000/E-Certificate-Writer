# E-Certificate-Writer
- Useful for writing names of participants on E-Certificates using Python3.
- Returns the certificates in PDF format.

## Virtual Environment Set Up

```sh
pip install virtualenv
virtualenv environment-name
```

## Repository Set Up

```sh
git clone https://github.com/aashish2000/E-Certificate-Writer.git
cd E-Certificate-Writer
pip install -r requirements.txt
```

## Files Required

- Certificate Template in .png format
- File containing names of Participants in .csv format
- Required Font Face file in .ttf format

##  Usage

```sh
python3 writeCertificates.py
python3 emailSend.py
```

- Enter all the required details for positioning and writing the text
- The final certificates are stored as pdf files in the Output Directory
- All certificates can be bulk emailed after adding them in the participant_email.csv
