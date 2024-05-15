HEADER_INFO = """""".strip()
SIDEBAR_INFO = """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="">Mohammed Ammaruddin</a>
<a class="contributor comma" href="">Manav S</a>
<a class="contributor comma" href="">Pratham Singh</a>
<a class="contributor comma" href="">Pratham Sharma</a>

</div>
"""
CHEF_INFO = """
<h2 class="font-title">Welcome to our lovely restaurant! </h2>
<p class="strong font-body">
<span class="d-block extra-info">(We are at your service with two of the best chefs in the world: Chef Scheherazade, 
Chef Giovanni. Scheherazade is known for being more creative whereas Giovanni is more meticulous.)</span>
</p>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
Made For Capstone by Batch 39
</p>

<pre>[Inputs]
    {food items*: separated by comma}
     
[Targets]
    title: {TITLE} &lt;section>
    ingredients: {INGREDIENTS: separated by &lt;sep>} &lt;section>
    directions: {DIRECTIONS: separated by &lt;sep>}.
</pre>

<p>
  <em>In the cookbooks (a.k.a <a href="https://huggingface.co/datasets/recipe_nlg">dataset</a>), the food items were referred to as NER. </em>
</p>
<p>
This is recepie generation system which will be used with image recognition system
</p>

</div>
""".strip()
