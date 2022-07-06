import tweepy as tw
 
def OpenTwitter():
   api_key = "ZEn7a52oCkjkupjo5g9SbH866"
   api_secret = "R8K1VrcXRXnp7rQiu2ukkJ5ih5wiw0de5JOq4FbIDVAdiRW7Ui"
   access_token = "1536446282373513217-vvcmAABPDMXXqpcYQMwndERMQOB8OG"
   access_secret = "R3LNVDETMWOJmNC6CAATEfTyaZhMYJih4Dv7qHX6lpXyS"
  
   auth = tw.OAuth1UserHandler(api_key, api_secret, access_token,access_secret)
   api = tw.API(auth)
 
   try:
       api.verify_credentials()
       print('Successful Authentication')
   except:
       print('Failed authentication')
  
   return api
 
def CloseTwitter(handle):
   pass
 
def SendTweet(handle, status, pic):
   handle.update_status_with_media(status, pic)
 
def mainTweet(m,us,af):
   ourHandle = OpenTwitter()
 
   SendTweet(ourHandle, m+" -"+us, af)
   CloseTwitter(ourHandle)
