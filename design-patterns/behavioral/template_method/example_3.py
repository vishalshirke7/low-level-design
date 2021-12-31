def get_text():
    return "plain-text"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


def convert_to_text(data):
    print("[CONVERT]")
    return f"{data} as text"


def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):
    data = getter()
    print(f"Got `{data}`")

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print(f"`{data}` was processed")


def main():
    template_function(get_text, to_save=True)
    template_function(get_pdf, converter=convert_to_text)
    template_function(get_csv, to_save=True)


main()