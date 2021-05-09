# Best Doctors & Hospitals Tracker
![](/images/image1.JPG)
* Best doctors and hospitals tracker is the name of the project we have built and the name of the website is ```JEEVAN NAKSHA```.
* In our website you can register in three ways :-
   1. You can register as an User if you are a normal user/patient.
   2. You can register as a Doctor if you are a Doctor.
   3. You can register as a Hospital if you are a Hospital.
* In recent days, online mode is very common in every industry and many people or customers are willing to use the online mode to complete their work.
* It's been a hard time for some users who are searching for some best doctors or hospitals nearby them, so that they can save their effort of searching via offline mode.
* Our Website ```JEEVAN NAKSHA``` will provide the users this facility to search for the doctors or hospitals near by them.
* User can even have an **appointment** with a particular doctor they like from our website.
* Every section of our website will be explained in the following [Documentation](#documentation).

# Documentation
* [Project-Installation](#Project-Installation)
* [Authentication](#Authentication)
* [Registeration](#Registeration)
* [Search-Doctors](#Search-Doctors)
* [Search-Hospitals](#Search-Hospitals)
* [View-Profiles](#View-Profiles)
* [Update-Profiles](#Update-Profiles)
* [Reviews/Ratings](#Reviews/Ratings)
* [Make-Appointment](#Make-Appointment)
* [Contributers](#Contributers)

## Project-Installation
### Project Environment
#### Following are the list of softwares required for the environment.
* Python 3 or more
* Django 3 or more
* pycopg package from python
* pillow package from python
* HTML5, CSS, Node.js Support
* Version control (Git, Github)
* Postgre sql server and PgAdmin
### Installation
#### Step-1 
Clone this repository **[link](https://github.com/WAD-Team-Alpha/Hospital_Review_System.git)** using this command in your terminal/command prompt.
```
git clone https://github.com/WAD-Team-Alpha/Hospital_Review_System.git
```
#### Step-2 
Navigate to public folder and create a python file with name **email.py**.\
![](/images/Capture.JPG)
#### Step-3 
Inside the **email.py** file create the list of variables mentioned below and assign them accordingly.
* ```EMAIL_HOST_USER```     This variable is used to store the **email** of the website
* ```EMAIL_HOST_PASSWORD``` This variable is used to store the **password** for the email of the website
* ```EMAIL_HOST```          This variable is used to mention the type of host **In our case we use smtp.gmail.com**
* ```DEFAULT_FROM_EMAIL```  This variable stores the **default email** used by the website
* ```DB_PASSWORD```         This is the password of the database used in the **settings.py** file in public folder
#### Step-4
Before you run the project, make sure that you apply all the migrations to your database. If you are using postgre sql use the following **command**
```
python manage.py sqlmigrate (App_name) (migration_number)
```
Here ```App_name``` is the name of the app which has the migration with migration number ``` migration_number ```
**Note:** that you should use the above command only if you are using the sql based database as your backend otherthan **sqlLite3** which is *default* one.
After you should migrate all the migrations using the following **command**.
```
python manage.py migrate
```
#### Step-5
After applying all the migrations, now its time to run the website. Make sure that you have your environment ready with all the mentioned softwares installed. In your command prompt/terminal run this command to start the **django server**.
```
python manage.py runserver
```

Hence the **installation** and setup of the project is **done completely**.

## Authentication

### How can a person signin. Follow these steps to signin:

![signin-image-alt](/images/Signin.png)
* Press ```signin``` button to get signed in.
* Enter valid user credentials of your account and press ```sign in```.If you do not have an account, the create one by pressing on create one link. If you entered wrong credentials then you be redirected to ```signin fail page```.
* On successfull login you will get back to index page . here the header is different for different kinds of user like ```public```, ```doctors``` and ```hospitals```. For doctors and hospitals they will get view profile button inplace of logout button.
* if user is an doctor or hospital manager then they get an ```view profile``` button.

![](/images/gif_signin.gif)

***

###  Steps to get signed out
* For user to get signed out you need to press `signout` button in home page.
* Where as for doctors and hospitals you need to navigate to their profile page and then press on **signout** button to get signed out.


![](/images/gif_signout.gif)

***

### What happens when a person forgets their ```password```. Here is the process for it.
![](/images/cap4.JPG)
* In the above screenshot we can see a ```forgot password?``` section. Clicking on that will redirect you to a page where we will ask your ```email``` which is linked with your **account**.
* Then after entering your mail, a ```password reset``` **link** will be sent to your **mail** Click on that link.
* After clicking on that link, Set your ```new password``` and click reset button.
* There you go. You have sucessfully **resetted your password**.
* Here is a small demonstration of the process.


![](/images/gif3.gif)
## Registeration
### A person can register in our website as follows
* If the person is a user or a patient, he can register using ```User Registeration``` form
* If the person is a doctor, he can register using ```Doctor Registertion``` form
* If the person has a hospital, he can register using ``` Hospital Registeration ```form
### Navigating to Signup page
* The page looks something **like this**


![](/images/cap2.JPG)
* Below is a small **Illustration** of how to navigate to signup page


![](/images/gif1.gif)

* You can register in any three of them depending on your ```profession```

***

### How to register in the website as a user
Below are the steps for registering as a ```User```:
* From Main page,go to ```SignIn``` page.
* For Registering as a new User click ```SignUp``` below forgot password.
* In signup page, click ```Signup as a user```.
* After clicking SignUp as a User, you will get a ```Registration form``` as shown below.


![UserRegForm](images/user_form.png)

* In User Registration Form, Fill all the details asked in the form and make sure the requirements are fulfilled like in Password it should contain a ```Capital letter and some special characters.```
* After filling all details required in the form click on ```Register Button```.
* After registering successfully, you will redirect to the ```main page``` with a message showing **Activate your account after clicking the link sent to your mail**.


![UserRegistration](images/user_reg.gif)

* Now, go to your ```registered mail``` and you can find a mail from ```jeevannakshawad``` with a **activation link** for your account.
* Click on that link, now you are succesfully registered as a User and you will be redirected to the ```main page``` with the message **Account Activated Succesfully**.


![activateAccount](images/activate_account.gif)

##### Now you're succesfully registered as a User.

#### Below are the some of errors you can encounter when you register
* If ```Password``` and ```Confirm Password``` are not same it will show **Passwords dont match** error. So make sure you enter the both passwords correctly.
* If any user registered with the ```same username``` before you register, it shows **UserName Already Exists**. So, Try with a different username.
* If any user registered with the ```same email``` before you register or if you're registering 2nd time with the same email, it shows **Email already Exists** error. So, make sure you enter your email correctly.

***

### How to register in the website as a Doctor

Below are the steps for registering as a ```Doctor```:
* From Main page, go to ```SignIn page```.
* For Registering as a new Doctor click ```SignUp``` button situated below ```forgot password``` option.
* In signup page, click Signup as a ```Doctor```.
* After clicking SignUp as a Doctor, you will get a ```Registration form``` as shown below.


![Doctor Registration Form](images/Docreg_form.png)

* In Doctor Registration Form, Fill all the details asked in the form and make sure the requirements are fulfilled like in Password it should contain a Capital letter, a small letter and some special characters and a ```minimum length of 8 charecters```.
* After filling all details required in the form click on ```Register Button```.
* After registering successfully, you will redirect to the ```main page``` with a message showing **Activate your account after clicking the link sent to your mail**.


![Doctor Registration](images/gif_docreg_3.gif)

* Now, go to your registered mail and you can find a mail from ```jeevannakshawad``` with a activation link for your account.
* Click on that link, now you are succesfully registered as a ```Doctor``` and you will be redirected to the main page with the message **Account Activated Succesfully**.


![activate Doctor Account](images/gif_docreg_2.gif)

#### Now you're succesfully registered as a Doctor.

#### Below are the some of errors you can encounter when you register
* If Password and Confirm Password are not same it will show ```Passwords dont match``` error. So make sure you enter the both passwords correctly.
* If any user registered with the same username before you register, it shows ```UserName Already Exists```. So, Try with a different username.
* If any user registered with the same email before you register or if you're registering 2nd time with the same email, it shows ```Email already Exists``` error. So, make sure you enter your email correctly.

***

### How to register in the website as a Hospital 
#### It is hospital registeration form ,hospital will register here
* From Main page, go to SignIn page.
* For Registering as a new Hospitals click SignUp button situated below forgot password option.
* In signup page, click Signup as a Hospitals.
* After clicking SignUp as a hospital, you will get a Registration form as shown below.



![](images/img4.png)
* In hospital Registration Form, Fill all the details asked in the form and make sure the requirements are fulfilled like in Password it should contain a Capital letter, a small letter and some special characters and a minimum length of 8 charecters.
* After filling all details required in the form click on Register Button.

* After registering successfully, you will redirect to the main page with a message showing Activate your account after clicking the link sent to your mail.



### It is demo how to register here 



![](images/reg.gif)
 * After registering successfully, you will redirect to the main page with a message showing Activate your account after clicking the link sent to your mail.
 * Click on that link, now you are succesfully registered as a Doctor and you will be redirected to the main page with the message Account Activated Succesfully.



## Search-Doctors

### You can Search by the following details of the ```doctors```:
  - ```First Name``` of the doctor
  - ```Last Name``` of the doctor
  - ```Specialization``` of the doctor
  - ```City``` where the doctor works
  - ```State``` where the doctor works
  - ```Pincode``` of the place where the doctor works
  
  
![DoctorSearch](images/doctor_search_bar.png)

* It is not necessary to know all the details listed above to search a ```Doctor```.
* You can search for a **doctor/doctors** by their ```first name``` or by their ```last name``` or ```City``` in which the doctor works.
* You can also search for **doctor/doctors** through the ```Pincode``` of a place where the doctor works.
* You can also see list of **Doctors** working in a particular state by selecting that ```state```.
* You can also see list of **Doctors** working in all ```States``` by selecting All option in search bar.
* You can also search for a doctor by their ```Specialization```.
* After entering details in the **doctor search bar** click on **Search** Button which will redirect you to **Doctor Search Results page**.
* If there are doctors found, you can see a ```list of with some information``` like Doctors ```Name,Department,Works at and Pincode and Ratings``` of the **doctor**. 
* If no doctors Found, then it shows **No Doctors Found**.


![DoctorSearchResults](images/doc-search.gif)

#### **You can also view the Doctor Profile by clicking View Profile Button**.

## Search-Hospitals

![Hospital search bar](images/Screenshot2.png)

### This feature helps the user to search for hospital using some filters.
#### The filters availble to search are:-
- ```Hospital name```
- ```Hospital registration number```
- ```Town/vilage for area```
- ```City```
- ```Pincode```
- ```State```


### Search results
#### After pressing the search button, you will be directed to the search results page.
In this page you can see the ```cards``` of the hospitals based on filters applied. The information given on cards is as follows:-
- ```Profile photo``` of hospital to the left most
- ```Ratigs``` to the rightmost
- ```Location```
- ```Pincode```
- ```Chief medical officer```
- ```Phone number```
- ```Email```

![Hospital search bar gif](images/gif_HS.gif)

### You can also view the hospital prifile by clicking 'view profile' button

## View-Profiles

### Doctors-Profile
#### It is doctor profile , doctor can view profile and other how register in website they can view doctor profile using search bar 
 * From Main page, go to view profile.
 * See all doctor detail  

![](images/img3.png)

 * Doctor name ,hospital to belong
 * Specicalistion , Exprience 
 * Time of meet the patient  

#### It is doctor profile demo 
 * According to rating and review we can judge the service

![](/doc1.gif)


### Hospitals-Profile
#### It is Hospitals profile , Hospitals can view profile and other how register in website they can view Hospitals profile using search bar
 * From Main page, go to view profile.
 * See all Hospital detail  

 
![](images/img2.png)
  * Hospital name , Facilty in hospital
  * Doctor team, chief of doctor 
  * Update profile like hospital name, doctor team

#### It is Hospitals profile demo


![](images/host1.gif)
 * According to rating and review we can judge the service

## Update-Profiles

### hospital and Doctor can update their profile
 * From profile page, go to update button.
 * Check use is doctor then update his profile and if it is user they can not update
 * Check use is Hospital then update his profile and if it is user they can not update
![](images/img5.png)
* update Doctor and Hospital name
* update Profile photo
* update Specicalistion , Exprience
### It is  update  Demo
![](images/update.gif)
* After update profile redirect in profile and get massage to update profile 

## Reviews/Ratings

### How to view reviews and ratings

* For viewing reviews and Ratings you need to scroll down in the profile page for a perticular doctor/hospital. Press ```load more``` button to load more reviews.


![myimage-alt-tag](/images/reviews.png)

* You can also see ```ratings summary``` in the same page.Here you can see the details like number of reviews added and average rating and also you can observe count of each rating added.


![myimage-alt-tag](/images/view_rating.png)

### How to add ratings an reviews


![myimage-alt-tag](/images/gif2.gif)

* In profile pages, you can add reviews and ratings in allotted slot, but you must get **logged in before hand**. otherwise page will shown like this.


![myimage-alt-tag](/images/review_signin.png)
* Another important thing is you must **signed with an user account** to add an review. After successful signin you can add review.


![myimage-alt-tag](/images/adding_review.png)
* After sucessfully adding review you can see your review in the reviews section (updates instantly).


![myimage-alt-tag](/images/added_review.png)

## Make-Appointment
![](/images/cap3.JPG)
### Only a patient can have an appointment with a doctor
* Patient first needs to give the username of the doctor by viewing the ```username``` from the respective ```Doctor profile```
* Then he must mention the ```date of the appointment```
* And then mention the ```message``` required to convey his/her problem to the doctor
* Once the appointment is done, An email is sent to **both the respective doctor and the user** just for the confirmation.
* And then, the doctor will take up the converstaion with the user. This is the complete process of the appointment.


![](/images/gif2.gif)
## Contributers
<table>
  <tr>
    <td align="center"><a href="https://github.com/surya0180"><img src="https://avatars1.githubusercontent.com/surya0180" width="100px;" alt=""/></a><br /><sub><b>Surya Teja</b></sub></td>
    <td align="center"><a href="https://github.com/bannu0snake"><img src="https://avatars1.githubusercontent.com/bannu0snake" width="100px;" alt=""/></a><br /><sub><b>Mahaboob</b></sub></td>
    <td align="center"><a href="https://github.com/prathyush11"><img src="https://avatars1.githubusercontent.com/prathyush11" width="100px;" alt=""/></a><br /><sub><b>Prathyush</b></sub></td>
    <td align="center"><a href="https://github.com/sekharsa"><img src="https://avatars1.githubusercontent.com/sekharsa" width="100px;" alt=""/></a><br /><sub><b>Sekhar</b></sub></td>
    <td align="center"><a href="https://github.com/satyamsingh-sg"><img src="https://avatars1.githubusercontent.com/satyamsingh-sg" width="100px;" alt=""/></a><br /><sub><b>Satyam Kumar</b></sub></td>
  </tr>
</table>
