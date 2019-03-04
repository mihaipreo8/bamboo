# bamboo
The @BL Code Challenge

Instructions on how to run the solution:
1. You have to have python and django installed on your machine. Due to some functions that were used, it is needed to have at least Python3.6 version and Django2.1 version. If using a Linux system, just execute the following commands for installing them:
		- sudo apt-get install python3.6
		- pip3 install django (if pip3 is not installed, please firstly install pip3)

2. For compatibility, please make sure you have the django-crispy-forms and pillow installed. For installing these two please run the following commands in the terminal:
		- pip3 install django-crispy-forms
		- pip3 install pillow

3. For executing the project, the server should be running in the first place. Please, open in terminal the "bambank_project" folder and run the following command: 
		- python3 manage.py runserver

4. Open your favourite browser and navigate "localhost:8000/login/" or "localhost:8000". 

NOTE: If you want to access the admin page of the web application, in order to be able to modify user rights, user details, transaction details and much more please use the following credentials:
		- Username: mihai  Password: bamboopanda


Comments:
1. This is not a full working solution as it was mentioned a time limit for this project. However, I have to admit that I worked a bit more than the established time limit for this project.

2. Due to the short amount of time, I did not write any type of TESTS. But, personally I do think that writing TESTS is a crucial matter when developing software. 

3. It was used some bootstap code from online sources. 

4. The Django predefined security functions were used for assuring the security during the Login and Register. But for example, for the situation in which a new bank payment/transaction is posted, I do consider that a better approach in terms of security would be to send the information to an HTTP page and from there to the database. The reason for that is to be able to implement some PREPARED STATEMENTS functionality in order to avoid any type of SQL Injection attack. Basically to send the post request to the database with all the fields blank and just then compleating the fields with the provided information. Thus any SQL Injection attack will not be effective. 

5. As long as the bank is running a promotion giving all new customers 100 free Bambeuros when they sign up, this might be a good chance for some people to try earning some extra money by cheating. Thus, on a real case scenario, the security should be very well developed for not allowing a person to register for more than one account. 

   As long as any individual would be able to create as many email addresses (containing fake details) as he/she would like, and as long as a MAC address of any device (no matter if PC, laptop, cellphone) can be changed, the email and MAC filtering will not represent a good way of enhancing security for the current problem. Thus, a good method of doing this is to ask the person trying to register of submitting a photo of an official document (passport) along with a short recording of himself/herself in which the face of that individual is visible and clear. Then, a match will be performed between the document and the recording using some face-recognition algorithms.

   Furthermore, I believe that it will also be important of not allowing to any legitimate new user to withdraw the money right after the registration was successful or even more, not withdrawing before doing a couple of online transactions. Thus, will be avoided that lots of new users will actually register just for earning 100 bambEuros. 
 