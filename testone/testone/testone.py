"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import random  
from random import sample 
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment


class TestoneXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = str(
        
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    
    def author_view(self, context=None):
        """
        The primary view of the TestoneXBlock, shown to Teachers
        when viewing courses.
        """
        html = self.resource_string("static/html/testoneTeacher.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testone.css"))
        frag.add_javascript(self.resource_string("static/js/src/testone.js"))
        frag.initialize_js('TestoneXBlock')
        return frag

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TestoneXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/testoneTeacher.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testone.css"))
        frag.add_javascript(self.resource_string("static/js/src/testone.js"))
        frag.initialize_js('TestoneXBlock')
        return frag


    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, req, pregunta, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'
	preguntas = ['Polinesia1','Polinesia2','Polinesia3','Polinesia4','Polinesia5','Polinesia6','Polinesia7','Polinesia8','Polinesia9','Polinesia0']
	prueba = sample(preguntas,k=4)
        self.count = prueba
        #return {"count": self.count}
	return {"count": prueba[0]}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TestoneXBlock",
             """<testone/>
             """),
            ("Multiple TestoneXBlock",
             """<vertical_demo>
                <testone/>
                <testone/>
                <testone/>
                </vertical_demo>
             """),
        ]
