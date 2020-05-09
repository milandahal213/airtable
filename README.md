# airtable


<details>
<summary>Creating account - Creating Base </summary>

<h3> 1. Go to https://airtable.com </h3>
</br>
</br> 

![login screen](/images/airtable_welcome.png)

</br>
</br>

<h3> 2. Sign in if you have an Airtable account, or Sign up to create a new account</h3>
</br>
</br> 

![sign up screen](/images/signup.png)![sign in screen](/images/signin.png)

<h3> 3. Click on Add a base and Start from scratch   </h3>     

![add base screen](/images/addbase.png)

<h3> and give it a suitable name</h3> 

![name base screen](/images/namebase.png)
        
<h3> 4. This will open up your new document . Note the names of the Table and Fields </h3>
        
![table view screen](/images/tableview.png)
</details>



<details>
  <summary>Finding the BaseID </summary>

<h3> 1. Go to https://airtable.com/api </h3>

![api welcome screen](/images/apiwelcome.png)

<h3> 2. Click on your project name to reveal the api page. Copy the BaseID and replace the "BaseID" in secrets.py with this string </h3>

![api page screen](/images/apipage.png)

</details>



<details>
  <summary>Creating the API Key</summary>


<h3> 1. Go to https://airtable.com/account and click Generate API Key</h3>

![api welcome screen](/images/apikey1.png)

<h3> 2. Copy the API Key and replace the "AirtableAPPKey" in secrets.py with this string. Do not share this string.</h3>

![api welcome screen](/images/apikey2.png)

</details>

<details>
  <summary>Using the library</summary>


<h3> 1. Edit the secrets.py file</h3>

Edit the secrets.py file by replacing BaseID and API Key from your account. Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> on how to do it.

<h3> 2. Check the demo.py file</h3>
</details>
