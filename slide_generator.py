from jinja2 import Environment, FileSystemLoader
import markdown
import os

# Set up Jinja2 environment
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

def render_slide(template_name, args):
    """Helper function to render a slide template."""
    try:
        template = env.get_template(f"{template_name}.html")
        html_args = [markdown.markdown(arg, extensions=['extra']) for arg in args]
        return template.render(args=html_args)
    except Exception as e:
        print(f"Error rendering {template_name}: {e}")
        return ""

def cover(args):
    print(f"🎨 Cover function called with: {args}")
    return render_slide('cover', args)

def about_me(args):
    print(f"🧑‍💻 About Me function called with: {args}")
    return render_slide('about_me', args)

def title_list(args):
    print(f"📜 Title List function called with: {args}")
    return render_slide('title_list', args)

def title_text(args):
    print(f"📝 Title Text function called with: {args}")
    return render_slide('title_text', args)

def title_image(args):
    print(f"🖼️ Title Image function called with: {args}")
    return render_slide('title_image', args)

def singular_paragraph(args):
    print(f"📄 Singular Paragraph function called with: {args}")
    return render_slide('singular_paragraph', args)

def to_do(args):
    print(f"✅ To-Do function called with: {args}")
    # print args for debugging
    newargs = []
    for i, arg in enumerate(args):
        print(f"  Argument {i}: {arg}")
        # check if the argument is a markdown heading
        if arg.startswith("## "):
            newargs.append(arg)
        if arg.startswith("- [ ] "):
            # add the to-do item to the list of todos
            todo_item = arg[6:]
            newargs.append("◻ " + todo_item)
        elif arg.startswith("\t- [ ] ") or arg.startswith("  - [ ] "):
            # add the nested to-do item to the list of todos
            # strip the indentation and "- [ ] "
            if arg.startswith("\t- [ ] "):
                todo_item = arg[7:]
            else:
                todo_item = arg[8:]
            # append a tab character to indicate it's a nested item
            todo_item = "&nbsp;" * 4 + "◻ " + todo_item
            newargs.append(todo_item)
    # print the todo list for debugging
    return render_slide('to_do', newargs)

def big_text(args):
    print(f"🔠 Big Text function called with: {args}")
    return render_slide('big_text', args)


def group_of_two(args):
    print(f"👯 Group of Two function called with: {args}")
    # this slide expects five arguments: left title, left content, 
    # optional connector, right title, right content
    return render_slide('group_of_two', args)

def group_of_three(args):
    print(f"👨‍👩‍👧 Group of Three function called with: {args}")
    return render_slide('group_of_three', args)

def group_of_four(args):
    print(f"👨‍👩‍👧‍👦 Group of Four function called with: {args}")
    return render_slide('group_of_four', args)

def big_text_small_image(args):
    print(f"🌆 Big Text Small Image function called with: {args}")
    return render_slide('big_text_small_image', args)

def loop_list(args):
    print(f"🔄 Loop List function called with: {args}")
    return render_slide('loop_list', args)

def just_image(args):
    print(f"🏞️ Just Image function called with: {args}")
    return render_slide('just_image', args)

def sign_off(args):
    print(f"👋 Sign Off function called with: {args}")
    return render_slide('sign_off', args)

