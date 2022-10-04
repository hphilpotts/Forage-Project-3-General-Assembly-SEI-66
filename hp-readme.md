# Pinterest-type App - Django-SQL       

## GA London SEI-66 Project 3: Django Framework, postgreSQL Database         

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

Now protecting routes:

