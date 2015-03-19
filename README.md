About the Python Properties Reader
==================================

PythonPropertiesReader is designed to easily parse and use Java Properties files in Python. In basic functionalities, it is equivalent to java.util.Properties class. It reads a property list (key and element pairs) from the input character stream in a simple line-oriented format. Lines are read from input until the end of the stream is reached. 

It returns the dictionary data structure populated with key value pair from properties file, so one can use any function supported by python dictionary data structure.

Any white space at the start of the following line have no affect on the key or element values.  Note that it is not sufficient to only examine the character preceding a line terminator sequence to decide if the line terminator is escaped; there must be an odd number of contiguous backslashes for the line terminator to be escaped. Since the input is processed from left to right, a non-zero even number of 2n contiguous backslashes before a line terminator (or elsewhere) encodes n backslashes after escape processing. 

As an example, each of the following three lines specifies the key "Truth" and the associated element value "Beauty":

          Truth = Beauty
          Truth:Beauty
          Truth                    :Beauty
 
As a third example, the line: 

          cheeses

specifies that the key is "cheeses" and the associated element is the empty string "". 


Features:

1. key termination characters-  "=" and ":"
2. All of key termination characters may be included in the key by escaping them with a preceding backslash character; for example,
  
          \:\=  would be the two-character key ":=".
		 
3. Any white space at the start of the following line have no affect on the key or element values.
As an example, each of the following three lines specifies the key "Truth" and the associated element value "Beauty": 
 
          Truth = Beauty
          Truth:Beauty
          Truth                    :Beauty
	   
4. Comment line or comment after key value pair will be ignored.
       
	   As an example first line will be ignored and second line specifies the key "Truth" and he associated element value "Beauty",  trailing comment will be ignored.
	   
	    #this is property file
        Truth :   Beauty   #do not change
		
Usage: 
              
			  import properties
              props = properties.loadproperties('python.properties')
              print props
              print props.get('fast\\')
              print props.get('Truth')

check the python.properties file.
 
     output:
	         {'cheese': '', 'easy=open': 'fast', 'fast\\': 'and  =  furious', 'python:easy': 'powerful', ':===': 'fantastic', 'Truth': 'Beauty', 'time': 'present'}
             
			 and  =  furious
             Beauty
