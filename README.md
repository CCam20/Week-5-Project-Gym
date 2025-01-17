# Week-5-Project-Gym
<hr>
<h1>Completed Features</h1>
<li>Allows the gym to create and edit Members
<li>Allows the gym to create and edit Classes
<li>Allows the gym to book members on specific classes
<li>Show a list of all upcoming classes
<li>Show all members that are booked in for a particular class
<li>Show warning if class is full or member is already booked in
<hr>
<h1>To do</h1>
<li><s>Delete bookings from Members page/Delete Members from Classes</s>
<li>Activate and deactivate members and classes
<li>Make use od standard and premium memberships

<hr>
<h1>Uses</h1>
<p>View Members via the members tab and add new members through form submission</p>
<p>View Classes via the classes tab and add new classes through form submission</p>
<p>View specific members/classes but clicking on names of each, delete or edit members/classes</p>
<p>View all booking via Enrollment tab</p>

<hr>
Programs used: Psycopg2, Flask,  Python, Html, Jinja

Run:
<li>Drop/Create Db gym_manager
<li>Create Tables with "psql -d gym_manager -f db/gym_manager"
<li>Populate tables with console.py
<li>Run flask with "flask run"

<hr>
<h1>Screenshots</h1>

![main_screen](/screenshots/MainPage.png)
![members_screen](/screenshots/MembersPage.png)
![classes_screen](/screenshots/ClassesPage.png)
![bookings_screen](/screenshots/BookingsPage.png)
![edit_screen](/screenshots/EditMemberPage.png)
![member_info_screen](/screenshots/MemberInfo.png)
