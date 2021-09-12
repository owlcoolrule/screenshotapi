**ScreenShotted**

A free API for taking screenshots. If you don't want to self-host, use our 100% free API here - https://owlcoolruleroblox.gitbook.io/screeenshotted/

Here's how to setup and self-host:
**1.** Download your Google Cloud authorization keys. Learn how here - https://cloud.google.com/translate/docs/setup

🛑 WAIT! Did you enable the permissions required for this to work? You'll need this key to have the "Storage Admin" permission enabled for the service account.

**2.** Open the .env file and change the value for _CLOUD_KEY_ to the path to your service account file.

**3.** Change the value for _BUCKET_ to the name of the Cloud Storage bucket you want to upload screenshots to.

**4.** Change the value for _CLOUD_URL_TEMPLATE_ to the template for URLs. Replace where you want the filename to be with {filename}. If you're using a public Cloud Storage bucket, set the value to this: `https://storage.googleapis.com/bucketname/{filename}`.

**3.** You're all done!

🛑 WAIT! Can you pitch in to help host our API? Sponoring this GitHub is a great way to chip in and support the hosting of this project. Thanks!
