<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>CS551Q_Assignment_3</h1>
<h3>What is this?</h3>
<p>This <code>README.md</code> file shows the instructions for running the solo Django project <strong>OpenReads</strong> — a book ordering web application developed as part of the solo assignment for Enterprise Software Development.</p>
<h1>Use of <script> in Templates</h1>
<p>This project strictly follows the instruction that no <code>&lt;script&gt;</code> tags or JavaScript were used in any of the templates. All visualizations and interactivity, including charts for admin dashboards, were rendered using Python libraries such as <code>matplotlib</code> and <code>seaborn</code>.
<br  />All client-side functionality was achieved through Django templating and Python server logic. No JavaScript or front-end scripting was required or included.</p>
<h1>How to run (with PYTHONANYWHERE)</h1>
<p>Please visit this URL to access the deployed app:
<br  /><strong>https://Durga19.pythonanywhere.com</strong></p>
<p>We've prepared two accounts:
<br  />Ordinary Account → [username: <code>Durga</code>, password: <code>durga12345</code>] — (This is the user account credentials and it works for both <strong>Codio and PythonAnywhere</strong>)
<br  />Codio Admin Account → [username: <code>codio</code>, password: <code>assignment</code>] — (This is the admin credentials and it only works for <strong>Codio</strong>)
<br  />PythonAnywhere Admin Account → [username: <code>durga19</code>, password: <code>Codio@12</code>] — (This is the admin credentials and it only works for <strong>PythonAnywhere</strong>)
<br  />With the admin account, you can view admin dashboard statistics and manage books, users, and orders.</p>
<h1>How to run through codio (local version)</h1>
<p>Use these commands:</p>
<pre><code class="bash">cd openreads-django-solo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
</code></pre>
<p>Finally, visit this URL:
<br  /><strong>https://your-codio-box-url:8000</strong></p>
<h1>Preparations in advance if you are going to edit the assignment files</h1>
<h3>Get python version 3.10.7</h3>
<p>When you open the Codio workspace, check your Python version:</p>
<pre><code class="bash">python --version
</code></pre>
<p>If it's <code>2.7.x</code>, install Python 3.10.7:</p>
<pre><code class="bash">pyenv install 3.10.7
</code></pre>
<p>If you get an error like <code>python-build: definition not found: 3.10.7</code>, then update pyenv:</p>
<pre><code class="bash">cd ~/.pyenv
git pull
</code></pre>
<p>Go back and install again:</p>
<pre><code class="bash">cd -
pyenv install 3.10.7
pyenv rehash
</code></pre>
<h3>Download files from GitHub repository</h3>
<p>This project is hosted on GitHub. Clone it using:</p>
<pre><code class="bash">git clone https://github.com/durga-0219/openreads-django-solo.git
</code></pre>
<p>Move into the folder and activate your environment.</p>
<h3>Get sqlite version 3.49.1</h3>
<p>To check:</p>
<pre><code class="bash">sqlite3 --version
</code></pre>
<p>If outdated, use the <code>sqlite-autoconf-3490100</code> folder (if provided) or manually upgrade SQLite:</p>
<pre><code class="bash">cd sqlite-autoconf-3490100
./configure --prefix=$HOME/sqlite
make
make install
</code></pre>
<p>Set your environment:</p>
<pre><code class="bash">export PATH="$HOME/sqlite/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/sqlite/lib"
</code></pre>
<p>Verify the new version again:</p>
<pre><code class="bash">sqlite3 --version
</code></pre>
<h1>Usage of Templates</h1>
<p>All templates and their usage are listed here:</p>
<ul>
<li><code>404.html</code> and <code>500.html</code> – error control pages</li>
<li><code>book_list.html</code> – shows list of books with filters</li>
<li><code>book_detail.html</code> – shows full details about a book</li>
<li><code>login.html</code> – login page</li>
<li><code>register.html</code> – registration page</li>
<li><code>cart.html</code> – displays cart items and total price</li>
<li><code>order_success.html</code> – confirmation page after order</li>
<li><code>custom_admin_dashboard.html</code> – admin stats and filters with matplotlib</li>
<li><code>user_list.html</code> – shows all registered users to admin</li>
<li><code>order_list.html</code> – shows all orders to admin</li>
<li><code>admin_book_list.html</code> – shows all books to admin</li>
<li><code>add_book.html</code>, <code>update_book_price.html</code> – admin book management</li>
</ul>
<h1>Data sources</h1>
<p>The dataset used in this project comes from Kaggle:
<br  />📚 <a href="https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset">Book-Crossing Dataset by Ruchi Bhatia</a></p>
<p>From this dataset, the <code>BX_Books.csv</code> file was used as the primary source of book data.
<br  />✅ The dataset was <strong>cleaned and reduced</strong> to include only relevant fields such as:</p>
<ul>
<li>Book title</li>
<li>Author name</li>
<li>Year of publication</li>
<li>ISBN</li>
<li>Publisher</li>
<li>Price (randomly assigned for demonstration)</li>
</ul>
<p>👉 The final version used in the app was saved as openreads_books_5000.csv after cleaning and selecting 5000 meaningful book records for performance and quality.</p>
<h1>Cleaning the Dataset and Reasoning Behind Reducing our Dataset.</h1>
<h3>What was done</h3>
<ul>
<li>Removed duplicates and entries with missing titles or authors</li>
<li>Normalized year, and price fields</li>
<li>Cleaned inconsistent author and publisher names</li>
</ul>
<h3>Reasoning</h3>
<ul>
<li>To simplify querying and admin management</li>
<li>To ensure clean visualizations on dashboards</li>
<li>To make the dataset light and efficient for a solo Django project</li>
<li>To maintain a user-friendly browsing and ordering experience</li>
</ul>
<h1>Development</h1>
<ul>
<li>Implemented custom login, registration (<code>UserCreationForm</code>), and user role-based view protection</li>
<li>Built book browsing, detail views, cart management with quantity controls, and order placement (single &amp; bulk)</li>
<li>Developed a superuser-only admin dashboard with book/user/order stats, Seaborn/Matplotlib charts, CSV exports, and filtering by title/author/year</li>
<li>Designed and linked models: <code>Book</code>, <code>Author</code>, and <code>Order</code></li>
<li>Secured all views using <code>@login_required</code> and restricted admin tools to superusers</li>
</ul>
<h1>Implementation</h1>
<ul>
<li>Used Django QuerySets for dynamic filtering by title, author, and year</li>
<li>Displayed login, registration, and admin alerts using the messages framework</li>
<li>Collected static files via <code>collectstatic</code> for deployment</li>
<li>Deployed on PythonAnywhere with secure HTTPS and full CSRF protection</li>
</ul>
<h1>Deployment</h1>
<p>Deployed on PythonAnywhere using Django's WSGI setup, static file mapping, and HTTPS enforcement for CSRF protection.</p>
<h1>Summary</h1>
<p>OpenReads is a Django web application for browsing and ordering books using a cleaned open dataset. It includes authentication, admin dashboards, and dynamic features. The project meets all solo assignment requirements and is deployed on PythonAnywhere.</p>
<h1>The name in git-log</h1>
<p><code>durga-0219</code> is the GitHub username of the solo project author.</p>
</div>