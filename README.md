<a href="https://github.com/jajosheni/quickTurtle/" title="python Downloader"><img src="https://img.shields.io/badge/quick-Turtle-brightgreen.svg"></a>
<a href="https://instagram.com/detajist" title="instapage"><img src="https://img.shields.io/badge/follow-instagram-orange.svg"></a>
<a href="https://www.python.org/downloads/release/python-350/" title="use python3.5"><img src="https://img.shields.io/badge/version-python3.5-brightgreen.svg"></a>

<img src="https://i.postimg.cc/hv92FK56/turtle.png">

### Installation Instructions
<table class="tableblock frame-all grid-all spread data-line-12">
<colgroup>
<col style="width: 50%;">
<col style="width: 50%;">
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">Step</th>
<th class="tableblock halign-left valign-top">Command</th>
</tr>
</thead>
<tfoot>
</tfoot>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">1. Fork/Clone/Download this repo</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><code>git clone <a href="https://github.com/jajosheni/quickTurtle" class="bare">https://github.com/jajosheni/quickTurtle</a></code></p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">2. Navigate to the directory</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><code>cd quickTurtle</code></p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">3. Install the dependencies</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><code>python setup.py install ` or  `pip install -r requirements.txt</code></p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">4. Run the main.py script</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><code>python main.py</code></p></td>
</tr>
</tbody>
</table>


#### Use at your own risk
**=====================**

<img src="https://i.ibb.co/PznQ8rK/1.jpg">

#### 1.1 version:

  1. Input bugfix.
  2. Response & error handling.
  3. Retry downloading missing part.
  
  ISSUES:
  1. Starts chunk from the beginning if interrupted wasting downloaded data.
  2. Cannot see the progress.
  
#### 1.0 version:

One day I wanted to download a movie but the network was full of users,
so I needed to fully utilize it. 

  1. This program gets the length of the file,
  2. breaks it into equal chunks,
  3. downloads them simultaneously,
  4. merges them together into the final file.  
  
  ISSUES:
  1. Cannot resume chunks if interrupted.
  2. Cannot see the progress.

