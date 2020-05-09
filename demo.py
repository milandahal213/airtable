
import airtable

 # Put_AT adds a record in Field ("Name") in the Table ("Table 1") with the value ("Milan")
 # Table 1 is Table name
 # Name is Field name (of type one line string) and 
 # Milan is value, 
 # Function returns the record id for the updated record (useful for deleting)
          
record_id airtable.Put_AT('Table 1','Name','Milan') 


# Get_AT returns the last record from the Field ("Name") in the Table ("Table 1")
# Table 1 is Table name
# Name is Field name
a=airtable.Get_AT('Table 1','Name')   


# Get_AT_field returns the entire list of record from the Field ("Name") in the Table ("Table 1")
# Table 1 is Table name
# Name is Field name
# value [0] is the first record , [1] is second ,[-1] is the last record and so on

array=airtable.Get_AT_field('Table 1','Name')      



# Delete_AT deletes the  record with "record_id" from the Table ("Table 1")
# Table 1 is Table name
# record_id is record id
    
c=airtable.Delete_AT('Table 1',"record_id")             

print(record_id)    # prints the record id returned while updating the field    
print(a)            # prints the value of the last record of the field
print(c)            # prints the status of delete- true or false
print(array)        # prints the whole list of field 