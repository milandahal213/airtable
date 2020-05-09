import secrets
from urllib.parse import quote
import ujson, urequests


def AT_setup():
     urlBase = "https://api.airtable.com/v0/"
     Key = secrets.ATappkey
     headers = {"Accept":"application/json","Content-Type":"application/json","Authorization":"Bearer " + Key}
     return urlBase, headers

 # Put_AT adds a record in Field in the Table with the Value
 # Function returns the record id for the updated record (useful for deleting)
     
def Put_AT(Table,Field,Value):
     urlBase, headers = AT_setup()
     urlTag = urlBase + Field
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table) 
     propValue={"records": [{"fields": {  Field: Value}} ]}
     try:
          value = urequests.post(urlValue,headers=headers, json=propValue).text
          data = ujson.loads(value)
          result = data.get("records")[-1].get("id")
     except Exception as e:
          print(e)
          result = 'failed'
     return result

# Get_AT returns the last record from the Field in the Table

def Get_AT(Table,Field):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table) + "?view=Grid%20view"

     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          result = data.get("records")[-1].get("fields").get(Field)
     except Exception as e:
          print(e)
          result = 'failed'
     return  result

# Get_AT_field returns the entire list of record from the Field in the Table
def Get_AT_field(Table,Field):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table) + "?view=Grid%20view"

     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          result=['']
          for i in data.get("records"):
              print(i.get("fields").get(Field))
              result.append(i.get("fields").get(Field))
          
     except Exception as e:
          print(e)
          result = ['failed']
     return  result

# Delete_AT deletes the  record with record id ID from the Table
#returns true if delete successfull
def Delete_AT(Table,ID):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table) + "?" + "records[]=" + quote(ID)
     print(urlValue)
     try:
          value = urequests.delete(urlValue,headers=headers).text
          data = ujson.loads(value)
          print(data)
          result = data.get("records")[-1].get("deleted")
     except Exception as e:
          print(e)
          result = 'failed'
     return  result
