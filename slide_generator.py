import markdown

def cover(args):
    print(f"🎨 Cover function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def about_me(args):
    print(f"🧑‍💻 About Me function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def title_list(args):
    print(f"📜 Title List function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def title_text(args):
    print(f"📝 Title Text function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def title_image(args):
    print(f"🖼️ Title Image function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def singular_paragraph(args):
    print(f"📄 Singular Paragraph function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def to_do(args):
    print(f"✅ To-Do function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def big_text(args):
    print(f"🔠 Big Text function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def group_of_two(args):
    print(f"👯 Group of Two function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def group_of_three(args):
    print(f"👨‍👩‍👧 Group of Three function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def group_of_four(args):
    print(f"👨‍👩‍👧‍👦 Group of Four function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def big_text_small_image(args):
    print(f"🌆 Big Text Small Image function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def loop_list(args):
    print(f"🔄 Loop List function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def just_image(args):
    print(f"🏞️ Just Image function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)

def sign_off(args):
    print(f"👋 Sign Off function called with: {args}")
    html_args = [markdown.markdown(arg) for arg in args]
    return "".join(html_args)
