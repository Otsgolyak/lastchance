def traverse_dir(dir, indent_level=0):
    import os

    for name in os.listdir(dir):
        if not name.startswith("."):
            try:
                path = os.path.join(dir, name)
                prefix = indent_level*(" "*4)
                if os.path.isfile(path):
                    print("%s (%d bytes)" % (prefix + "╰─── " + name,
                                             os.path.getsize(path)))
                else:
                    print(prefix + name + ":")
                    traverse_dir(path, indent_level+1)
            except Exception as ex:
                print(ex)
traverse_dir(r"C:\Users")