from flask import Flask
app = Flask(__name__)



@app.route("/home")
@app.route("/")
def hello():
    return """  <!DOCTYPE html>
  <html lang="en">
  <head>
  <title>CSS Template</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
  * {
    box-sizing: border-box;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
  }

  /* Style the header */
  header {
    background-color: #666;
    padding: 30px;
    text-align: center;
    font-size: 35px;
    color: white;
  }

  /* Create two columns/boxes that floats next to each other */
  nav {
    float: left;
    width: 30%;
    height: 300px; /* only for demonstration, should be removed */
    background: #ccc;
    padding: 20px;
  }

  /* Style the list inside the menu */
  nav ul {
    list-style-type: none;
    padding: 0;
  }

  article {
    float: left;
    padding: 20px;
    width: 70%;
    background-color: #f1f1f1;
    height: 300px; /* only for demonstration, should be removed */
  }

  /* Clear floats after the columns */
  section:after {
    content: "";
    display: table;
    clear: both;
  }

  /* Style the footer */
  footer {
    background-color: #777;
    padding: 10px;
    text-align: center;
    color: white;
  }

  /* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
  @media (max-width: 600px) {
    nav, article {
      width: 100%;
      height: auto;
    }
  }
  </style>
  </head>
  <body>


  <section>
    <nav>
      <ul>
        <li><a href="#">London</a></li>
        <li><a href="#">Paris</a></li>
        <li><a href="#">Tokyo</a></li>
      </ul>
    </nav>

    <article>
      <h1>London</h1>
      <p>London is the capital city of England. It is the most populous city in the  United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>
      <p>Standing on the River Thames, London has been a major settlement for two millennia, its history going back to its founding by the Romans, who named it Londinium.</p>
    </article>
  </section>

  <footer>
    <p>Footer</p>
  </footer>

  </body>
  </html>
"""

# url
# view

@app.route("/aboutus")
def about():
	return "<h1>This is About Page</h1>"

@app.route("/services")
def service():
    return """<!DOCTYPE html>
				<html>
				<body>

				<h2>Services</h2>
				<img src="https://www.w3schools.com/html/pic_trulli.jpg" alt="Trulli" width="500" height="333">

				</body>
				</html>"""

@app.route("/contactus")
def contact():
    return """ <!DOCTYPE html>
			<html>
			<body>

			<h2>Contact us</h2>

			<form action="">
			  First name:<br>
			  <input type="text" name="firstname" value="Enter ">
			  <br>
			  Last name:<br>
			  <input type="text" name="lastname" value="Enter  ">
			  <br><br>
			  <input type="submit" value="Submit">
			</form> 


			</body>
			</html>"""    


if __name__ == "__main__":
    app.run(debug=True)




