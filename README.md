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
   
<h3> 0. Download secrets.py and airtable.py to your EV3.</h3>


<h3> 1. Edit the secrets.py file</h3>

Edit the secrets.py file by replacing BaseID and API Key from your account. Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> on how to do it.

<h3> 2. Refer to demo.py file</h3>

<details>
<summary>Put_AT</summary>
        
Put_AT('Table_name','Field_name','Record_value') 
Put_AT function adds a record in the Field_name Field of the  Table_name Table with the value Record_value
The function returns the record id for the updated record (useful for deleting)

</details>
<details>
        
<summary>Get_AT</summary>

Get_AT('Table_name','Field_name') returns the last record from the Field_name Field of the Table_name Table.   

</details>
<details>
<summary>Get_AT_field</summary>
        
Get_AT_field('Table_name','Field_name') returns the entire list of record from the Field_name Field of the Table_name Table. The return value will be a list. Users will need to use indexing to access individual records. use [-1] to access the last record. 

</details>
<details>
<summary>Delete_AT</summary>

Delete_AT('Table_name',"record_id")  deletes the  record with "record_id" from the Table_name Table.

</details>
</details>
