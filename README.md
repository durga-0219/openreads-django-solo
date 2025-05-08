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
