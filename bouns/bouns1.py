contents = ["All carrots are to be sliced",
            "longitudianlly.",
            "The carrots were reportedly sliced.",
            "The slicicng proccess  well presents"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]
for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
