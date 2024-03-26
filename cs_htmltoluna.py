# While preparing for your first round interview with Asana, you start exploring Luna, Asana's in-house framework for automating Web application creation. For practice - and fun! - you decide to implement a simple HTML-to-Luna converter.

# To keep things straightforward, you will only consider 4 HTML tags: div, p, b, img. Here's how valid HTML is constructed:

# an empty string is valid HTML;
# <img /> is valid HTML (note the whitespace character between img and /);
# if HTML is valid HTML, then <div>HTML</div>, <p>HTML</p> and
# <b>HTML</b> are all valid.
# if HTML1 and HTML2 are both valid HTML, then HTML1HTML2 is valid HTML.
# For example, <div><p><img /></p><b></b></div> is valid HTML, but <div><p></div> is invalid.

# The conversion of each tag from HTML to Luna format is performed as follows:

# <div><arg1><arg2>...</div> → DIV([arg1, arg2, arg3, ... ]);
# <p><arg1><arg2>...</p> → P([arg1, arg2, arg3, ... ]);
# <b><arg1><arg2>...</b> → B([arg1, arg2, arg3, ... ]);
# <img /> → IMG({})
# Example

# For html = "<div><img /></div>", the output should be
# solution(html) = "DIV([IMG({})])";
# For html = "<div><p><img /></p><b></b></div>", the output should be
# solution(html) = "DIV([P([IMG({})]), B([])])";
# For html = "<div><p></p><p></p><p></p></div>", the output should be
# solution(html) = "DIV([P([]), P([]), P([])])";
# For html = "<div><img /><b></b><img /></div>", the output should be
# solution(html) = "DIV([IMG({}), B([]), IMG({})])".


def solution(html):
    substr=''
    result =""
    stack=[]
    
    for s in html:
        substr+= s
        print(substr)
        if substr =="<div>":
            stack.append(("</div>", []))
            substr=""
        elif substr =="<p>":
            stack.append(("</p>", []))
            substr=""
        elif substr == "<b>":
            stack.append(("</b>",[]))
            substr=""
        elif substr == "<img />":
            if len(stack)>0:
                stack[-1][1].append("IMG({})")
            else:
                result+="IMG({})"
            substr=""
           
        elif len(stack)>0 and substr == stack[-1][0]:
            completed_tag = return_luna(substr, ', '.join(stack[-1][1]))
            stack.pop()
            substr=""
            if len(stack)>0:
                stack[-1][1].append(completed_tag)
            else:
                result += completed_tag
    return result
            
def return_luna(closing, middle):
    if closing == "</div>":
        return f"DIV([{middle}])"
    if closing == "</p>":
        return f"P([{middle}])"
    if closing == "</b>":
        return f"B([{middle}])"
    
    
    