<h1>WebGraphix Project</h1>

WebGraphix is a website providing customers will be ability to purchase Logo packages, Website packages and even purchase a error fixing package if your website has an issue. We also have a custom order form for those projects bigger projects or smaller projects that do not meet the premade packages available, or you can use the custom order form just to get a quote.

<h2>UX</h2>

This website is designed for the customers who want to get their first website onto the internet or just want a brand to begin their journey on the internet. This website offers customers the chance to buy everything they need to get going on the web and truly bring their project to life.

As a graphics designer you would want to have a website to sell your designs and work, you would come to WebGraphix and ask us for a quote or buy our standard web design package and we can create that website for the graphics designer to get selling their hard work to their customers.

Our initial wireframe for WebGraphix was this one: https://www.mediafire.com/view/287so7k2r0xysz3/wireframewebgraphix.png/file

<h2>Features</h2>

<h3>Existing Features</h3>

Order form - Allows the customer to input their details and their budget and sends the data to the admin panel for staff to review the order.

Profile - Allows the customer to update their password and gives them the date/time as an additional feature.

Registration - Allows the customer to register an account and login to use the website.

Login - Allows the customer to login after they have registered

Forgot Password - Allows the user to reset their password

<h3>Features Left to Implement</h3>

Portfolio - Allow the customers to see passed work so that they feel comfortable purchasing off the store.

Additional customisation options in profile - Allow the customer to upload a profile picture and view their order history.

<h2>Technologies Used</h2>

We used the following technologies in this project:

<h3>Programming languages:</h3>

- HTML
- Javascript
- JQuery
- CSS
- Python

<h3>Frameworks used:</h3>

- Django
- Bootstrap
- Fontawesome

<h3>External sources used:</h3>

- Amazon Web Services (S3 Bucket)
- Heroku (Deployment platform)
- Github (For our version control)

<h2>Testing</h2>

We have done various testing across the website to ensure that it works as efficiently as possible.

1. Order form:
 i. Went to Order form
 ii. We tried submitting the order form
 iii. The form was submitted but no form was recorded in the admin panel
 iv. Checked the code and saw that in the admin.py we didnt register the contactform model
 vi. Rechecked the form and the orders were coming through successfully into the admin panel

2. Checkout:
 i. Added products to cart
 ii. Went to checkout
 iii. Adjusted items in cart, this worked as expected
 iv. Tried payment with Stripe in test, worked correctly
 
We have tested the site on mobile devices and the site works and looks as intended.

We did encounter few errors during development, one of the errors we discovered was right at the end when we were trying to deploy the project to Heroku, we had the error "Could not load Boto3's S3 Bindings. No module named 'boto3'". We identified that the reason this was coming up was because we hadn't added the boto3 to the requirements.txt, once this was sorted it fixed the issue.

<h2>Deployment</h2>

To deploy the project we used the Heroku platform, to do this we had to first host our static files externally as Heroku would not host these for us. For this we used Amazon Web Services S3 Bucket service, which we then pushed our static and media files to.

Our deployed version on Heroku uses the Postgres database rather than the SQL Lite 3 database we used locally, we can now use the Postgres locally and on Heroku but we had to rebuild the database for this.

We can run our code locally on Gitpod or by importing the Github code locally to another application such as Visual Studio. We then can use the command 'python3 manage.py runserver' to run the code.

<h2>Credits</h2>

Credits to https://unsplash.com/ for providing the images free of charge.
