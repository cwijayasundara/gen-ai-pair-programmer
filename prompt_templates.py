# Scenario 1: Improve existing code
prompt_template_improve_1 = """
Could you help enhance this code within its original programming language? You have expertise in this language.

{question}

Please provide a detailed explanation of the improvements made.
"""

prompt_template_improve_2 = """
I believe there might be better approaches to this code, given the programming language used.

You are proficient in this language.

{question}

Please investigate various solutions to the problem, and elucidate each.
"""

prompt_template_improve_3 = """
I believe there might be better approaches to this code, given the programming language used.

You have expertise in coding.

{question}

Please explore various solutions to the problem, and recommend the most suitable one for this scenario.
"""

# Scenario 2: Simplify code
prompt_template_simplify_1 = """
Could you help streamline this code within its original programming language?

You are proficient in coding.

{question}

Please annotate each line thoroughly,
and provide a detailed explanation of your modifications and the rationale behind them.
"""

# Scenario 3: Write test cases
prompt_template_unit_test_1 = """
Could you assist in generating unit test classes (e.g., JUnit for Java) for the provided code?

You possess expertise in coding, along with experience in both unit and integration testing.

{question}

Please elaborate on the objectives these unit test cases are intended to fulfill.
"""

# Scenario 4: Make code more efficient
prompt_template_efficient_1 = """
Could you enhance the efficiency of this code?

You are proficient in coding.

{question}

Please provide a thorough explanation of the modifications and the reasoning behind them.
"""

# Scenario 5: Debug your code
prompt_template_debug_1 = """
Could you assist in debugging this code?

You are adept at debugging.

{question}

Please elucidate your findings and explain why a particular issue was identified as a bug.
"""

# Scenario 6: Explain Code
prompt_template_explain_1 = """
Could you elucidate the functioning of this code?

You possess coding expertise.

{question}

Please delve into the details, ensuring clarity in your explanation
"""

# Scenario 7: Document Code

prompt_template_documentation_1 = """Please create a user-friendly technical documentation for this code, tailored to 
the programming language it's written in.

You have expertise in coding.

{question}

Present the documentation in Markdown format.
"""

prompt_template_documentation_2 = """
Please generate a UML sequence diagram utilizing Mermaid for the provided code:

You possess expertise in Mermaid, UML, and technical designs.

{question}

Render the output in Markdown format.
"""

prompt_template_documentation_3 = """
Please generate a UML class diagram using Mermaid based on the provided code:

You are proficient in Mermaid and technical designs.

{question}

Render the output in Markdown format.
"""

# Scenario 8: Code conversions
prompt_template_conversion_1 = """
Please convert this code to Python with the utmost efficiency, accuracy and in the most Pythonic way possible.

You are proficient in Python programming.

{question}

Render the output in Markdown format.
"""