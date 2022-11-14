<p align="center">
    <img src="readme/GA-header.png">
</p>

# 'Forage' : SEI Project 3        

## Description:     
<!-- TODO : link Helene and Ivan's GitHubs -->
This is a image-based, _Pinterest_-type 'mood board' web app, built as a team of three () in one week using Python within a Django framework, linked to PostgreSQL SQL database. Users can sign up, upload images, create mood boards and then link both their own or other users' images to theit 'boards' This project was completed as the third project for General Assembly London's Software Engineering Immersive course, and was presented to my Instructional Team and fellow SEI cohort on 07/10/22.          

My particular focus for this project was primarily on User functionality: signup, authentication and authorisation, profile CRUD operations and password reset. I also worked on formatting and _Materialize_ 'Toast' notifications for User feedback. This project was my first experience of working as a 'Team Member' (rather than Team Leader) within a group, and my first experience of working in a group of 3 or more developers.      

![Screenshot of the finished site](readme/apphomepage.png)     

## Links:       
[Deployment link](https://namesei66.herokuapp.com/)      
[Google Doc README](https://docs.google.com/document/d/1nJy5gzf3n5Jnp8f--a1C0feFb3mQ6IKMfbIpt3UtLls/edit?usp=sharing)      

## Getting started & Install:       

To use the app, please feel free to create an account (your real email is not required!) and start exploring.       

_Please note_ that at present, there is an issue with image upload where Heroku's ephemeral file storage deletes any newly uploaded images after less than 24 hours. As such, many of the image links are currently broken where uploaded files have been removed, and any images newly uploaded will not persist past a 24 hour period before breaking.

To contribute, please fork from GitHub and then run `pip install -r requirements.txt` to install the required dependencies, alternatively see `requirements.txt`, submitting a pull request for any completed contributions.        

## Technologies used:       
- Written using HTML5, CSS3, Python3 in Visual Studio Code.        
- Built using a Django framework linked to a PostgreSQL database.       
- Psycopg2 PosrgreSQL database driver, sqlparse SQL parser.         
- Materialize CSS library, Pillow Python imaging library.        
- Hosted on Heroku.     

## Brief & Project aims:       

The brief for this project was to create a Full Stack web application as a group, in one week, using Python, Django and PostgreSQL. Technical requirements included:        
- Use at least 2 related models, one of which being User, with all major CRUD operations required for at least one model.       
- Add authentication and authorisation to restrict access to appropriate users. Include signup, sign in, change password and logout functionality. Give user feedback after each action.     
- Layout and style frontend using clean and well-formatted CSS (and if required - use a framework for this).        

Stretch goals included:     
- Send verification email upon registration, allow password reset via email.        
- Allow users to upload images.     

The aim of the project was to consolidate two intensive weeks of learning the Python programming language and working with Django and SQL databases (specifically PostgreSQL). Further to this, this project allowed me to take what I had learned about group Git and working as a pair, and then apply this to working in a larger team of three - this time as a 'Team Member' rather than 'Team Leader'. Concepts covered included relational database modelling, Django Models, Class-based views and MVT architecture.          

## Key takeaways and learnings:       

I enjoyed this project as it was an opportunity to create a web app using a 'new' language after 6 weeks of JavaScript. I had spent some time self-teaching Python before starting the course - so had a bit of familiarity with its syntax - but crucially I found that the concepts and skills learned on JS translated across really quickly into Python having come back to it after a few months. Picking things up comparatively quickly was a great feeling!

It was a great experience working as a team of three for the first time, especially as we all had such different strengths and weaknesses (and indeed personalities and approaches!). Our 'team culture' was supportive and many of the challenges faced in Project 2 were much easier to overcome the second time around.      

Lastly, I had fun working with Django, especially using the 'baked in' functionality as compared to Express' more minimalist framework. I found it to be quick to pick up and I was a fan of the built-in admin app and auth features. Looking back, Python and Django seems somewhat 'alien' to me now, but I know that this project was great for my confidence, and has been a great foundation, putting me in a great place when I do revisit Python and Django in the future.        

Key learnings were as follows:      
- Git / GitHub repository setup and configuration are _extremely_ important. I got this wrong at the start of this project which meant that the structure and routines that I was used to for version control would not work as expected. This caused a lot of inital difficulty! By adapting my approach I was eventually able to find a way of working that overcame these difficulties.       
- Careful - and detailed - planning is key when working with SQL databases. 'In-flight' changes to the ERD can cause a lot of headaches: it is much better to spend the time getting this right from 'day one' rather than spending more time making changes later on.      
- Migrations can be - for lack of a better term - a nightmare when things go wrong! This led to occasional instances where we would 'break' our database and have to try and resuscitate it. By the same token, `__pycache__` files caused us a lot of unneccessary drama: it was only later in the project that we realised that our `.gitignore` file was key to minimising conflicts (as opposed to manual deletions of problematic files - _not the right way of doing things_!).        
- Configuring back-end email is not easy! Making the decision to go in a different direction and invest time into other features was the right one. That said, I would love to go back and get this working in future!      
- User Profile models are a powerful and effective way of adding functionality to the built-in User model. I am very glad that I chose this approach rather than the alternatives!        
- Leveraging individual strengths and talents is a great way of getting the most out of everyone. We did a great job of supporting each other in this way, by focusing on areas where we were more comfortable, and seeking help in areas where we were less comfortable.       

## Successes and Challenges:         

This project was as rewarding as it was challenging, with the confidence and knowledge gained as a result of overcoming challenges being the most important successes. The 'learns' above were amongst the most major successes, stemming from some of the most difficult aspects of or moments within the project. Some further 'wins' for me were:   

- Personally implementing User Profile models, along with all major CRUD functions. This covered the majority of technical requirements for the project; whilst challenging at times, it was also very rewarding - getting everything up and running was a great feeling and I really enjoyed working with authentication and authorisation for the first time on a project.        
- Gaining further confidence with CSS: I found work on styling notably easier this time around, and was able to produce better results much more quickly than I had in earlier projects. We were able to roll out much of the styling work completed on User Profile templates to other templates - being able to make this contribution represented, for me, a real step forward in my confidence and competence with CSS.     
- Getting really positive feedback from our Lead Instructor for implementing Materialize 'Toast' notifications. This was a challenging piece of work, and getting acknowledgment following the presentation that this was a complex (and given our experience, impressive) addition was a fantastic feeling and a real boost for my confidence!        
- Delivering a project that (despite many delays due to git issues) hit all technical brief requirements and is - Heroku image issue notwithstanding - largely bug-free was a real success, thanks largely to our careful planning and realistic expecations.       

Further to the challenges detailed in 'Key takeaways and learnings' above (particularly version control and migrations) other key challenges included:      

- Fully grasping the concepts around relationed SQL databases (having previously worked with NoSQL databases): in particular, properly 'getting' how join tables work and are used was difficult, especially at the start of the project when producing our ERD. I thought I understood these concepts before we started this project but soon found my understanding challenged! Happily though, this project was - as intended - a great way to condense and clarify my understanding of SQL concepts, and I came out of it with a much more robust grasp of these!       
- I found using Django Templating Language a real challenge at times: I would expect certain functionality seen in Python to also be available in DTL (when it wasn't), and I found the documentation / help articles / _stackoverflow_ answers to be a lot more sparse as compared to other technologies.     
- Implementing Toast message notifications as above took a lot of trial and error: I was able to get `<p>{{message}}</p>` to work, `[...] onclick.M.toast(‘I’m a toast message!’)[...]` to work, but not - as per the Materialize documentation - `<script>M.toast({html: "{{message}}", classes: 'green rounded', displayLength:2000});</script>` (instead getting 'M' is not defined). Finding the solution of including a `DOMContentLoaded` event listener within the script tag before running `M.toast` was a big moment as it was the first time I had come across 'synchronicity' issues: finally finding a solution without external help or guidance was perhaps the high point of the project despite it being a major challenge to resolve.           

## Bugs & Issues:       

- Uploaded images are lost (and therefore <img src=''/> links break) after <24 hours: this is due to Heroku's ephemeral filesystem.       
- 'Dark Mode' not yet working.      
- 'Not got an account?'..etc. message does not show up well against homepage background.        


## Future Improvements:           

- Fix uploaded image issue: either by re-hosting elsewhere or using storage such as S3 buckets.     
- Implement back-end email server in order to add email password reset/email verification.      
- Resolve some CSS responsiveness issues / styling snags.       

---         



_Rough notes of process to be converted to a lovely readme at a later date!_        

## Planning Stage 1, Day 01:        
29/09/22        

Team formed: Helene (Team Lead), Ivan and I. We have decided on a 'Pinterest-type' app for our project.     

### Early Planning stages:      
We have set up a Trello board to manage workflow, established a main Repo and forked successfully to Team Members. This has been something of a learning curve - having been Team Lead on the previous group project I have had to get used to the extra steps required when forking!           

Early Wireframe completed and ERD started. Advice taken on how to relation our tables. At one stage, we were deciding between a three-table join table (User, Image, Board) and three join tables. Eventually we decided upon a single join table for Image-Board M-M and 1-M for User-Image and User-Board.

## Planning Stage 2, Day 02:        
Site roadmap set up in Excel document,      

[add rest of Day 02 here]       

## Production Stage 1, Day 03:      

Decided to extend built-in Django User model by adding User Profile model linked One-One. Not yet tested working as Auth fnc. has not been added at this stage. Model added to `models.py`, with image upload fnc which will need to be tweaked once testing can begin.     
Created database in _pgAdmin4_ and successfully migrated, checked working ok in GUI.        

Starting on auth route. We'll need to go back later and update this path to a more interesting page than 'Home' one the right paths are set up. I've added this to Trello Board so that this doesn't get missed! Ditto `redirect` path in `signup` view.        

[git struggles in here]     

User details page added: R from Read!       

## Productions Stage 2, Day 04:     

Today, I decided to work on getting `Update_User_Form` and `User` properties to work before worrying about `Update_Profile_Form` and `Profile` Properties. An early breakthrough in this regard: I was able to get `User` properties to render, and then shortly after, `Profile` properties.        
After a bit of work and some minor mistakes I was finally able to get the `Update_User_Form` to work. I was struggling to get `Update_Profile_Form` to render - of course as soon as I sought advice and shared my screen I realised I could add as second form and input to the `profiles/detail.html` template. The form then renders ok!     
With a bit of tweaking (and using `enctype="multipart/form-data"`) I am now able to get both forms to render as one, with one submit button.        

Inital values populate into the `User` aspects of the form but do not populate into the `Profile` aspects. In order to get this to happen I have used:  

```
        profile_form = UpdateProfileForm(instance=request.user)
        profile_form.fields['user_bio'].initial = user.profile.user_bio
        profile_form.fields['user_profile_pic'].initial = user.profile.user_profile_pic
```     

In testing the form there has been a concerning development: I apprea to have somehow changed the superuser password. I believe the issue was caused when I was running both a regular user and superuser session at the same time. Reset by running a new `createsuperuser`.       

Another issue in testing: when creating a new user through the site (rather than admin panel), I got the following:     

```
RelatedObjectDoesNotExist at /users/5/
User has no profile.
```     

Documentation/articles suggest the requirement for a `signals.py` file which will create a User Profile whenever a `User` is created through `signup`. Added this, still getting the same issue. Overriding the `ready()` method in `AppConfig` within `apps.py` means that signals are registered and auto-profile funcionality is working.        

Issue found in testing: `User` values are being saved but `Profile` values are not. After some digging, I changed the following line:       

```
def profile_detail(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
            # -> was previously `[...] instance.request.user)`, did not save!
```     

`user.profile.user_bio` now saves. However, `user.profile.user_profile_pic` does not yet save. Tried lifting `upload_to` from the `Profile` model like so: `user_profile_pic = forms.ImageField(required=False, upload_to='profilepics')` but this throws `TypeError: Field.__init__() got an unexpected keyword argument 'upload_to'`.     

Tried the following in `Profile` model:     

```
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.user_profile_pic.path)

        if img.height > 100 or img.width> 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
```

No luck. Image upload works through `/admin/` and I've been able to get the image to save and then render in Profile details. The line `profile_form.fields['user_profile_pic'].initial = user.profile.user_profile_pic` was not initially worling when a file is added through `/admin/` but now seems to work, I'm not sure why this is!      

Again, a change of image is accepted but not saved. After reading the documentation, updating the `profile_detail` view with `request.FILES` as follows seemed to be the solution: `profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)` - and it works!       

Show/hide functionality added to User Profile form. I started working on User Delete functionality but got: `relation "main_app_board" does not exist` - will attempt to implement later if possible.       

Instead I have moved onto User Profile Index. Rudimentary index page added. Now adding 'view other user' page which will link from a user. This now works! I have not provided a link to users index at this stage as it is not needed.     

Getting errors when attempting to use newly merged Create Board / Create Image - lost migrations during merges, running `python3 manage.py migrate main_app` on a new DB fixed this.        

Now protecting User Profile routes: index restricted to staff only, profile detail views restricted to logged in users only, additionally the edit (and when implemented, delete) views restricted to users whose ID matches the user_id being acted upon.      

I'm now going to reattempt to add delete user functionality: it looks as if the issue seen before was caused by the migration issue. Now works with some tweaks to the additional user id check protection and a change from render to redirect.    

[rest of day 4]     

## Production Stage 3, Day 05:      

Issue found where newer images not rendering: this was where I had changed `MEDIA_ROOT` to set a target for profile pics, this in turn had changed where all uploaded images are saved. Image detail and image index pages were looking in `main_app/static` but images uploaded to `main_app/media` - src changed, issue resolved.     

Authorization protection added to views.        

Made minor formatting changes to base.html and confirmdelete.       

Now adding 'hero board' functionality to user pages which currently look like:      

[screenshot1]      

[rest of day 5]     

## Production Stage 4, Day 06:      

`UserSignupForm` added to `forms.py`, this inherits from the built-in `UserCreateForm` but also includes a `required=True` email field (needed for reset pw).       

After a morning of trial and error attempting email password reset, I am instead going to try in-site password changes (will not work for forgotten passwords!). Got this up and running fairly easily : I elected to use the built-in `PasswordChangeForm` within the `base.html` template (rather than - for example - using the Django CBV for this action).     

All forms checked as having {% csrf_token %}.       

I am now going to add user feedback for events using `messages`. Turns out that Bootstrap and Materialize do not get on together!       


