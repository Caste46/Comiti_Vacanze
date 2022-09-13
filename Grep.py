def grep(pattern, flags, files):
    flags = flags.replace(" ", "")
    flags = flags.replace("-", "")
    flags = list(flags)
    if "i" in flags:
        pattern = pattern.lower()
    res = ""
    for filename in files:
        with open(filename) as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if "i" in flags:
                    line = line.lower()
                curr = ""
                if "x" not in flags:
                    if "v" not in flags:
                        if line.find(pattern) != -1:
                            if "l" in flags:
                                res += f"{filename}\n"
                                break
                            curr = f"{lines[i]}"
                            if "n" in flags:
                                curr = f"{i + 1}:{curr}"
                            if len(files) > 1:
                                curr = f"{filename}:{curr}"
                    else:
                        if line.find(pattern) == -1:
                            if "l" in flags:
                                res += f"{filename}\n"
                                break
                            curr = f"{lines[i]}"
                            if "n" in flags:
                                curr = f"{i + 1}:{curr}"
                            if len(files) > 1:
                                curr = f"{filename}:{curr}"
                else:
                    if "v" not in flags:
                        if line == pattern + "\n":
                            if "l" in flags:
                                res += f"{filename}\n"
                                break
                            curr = f"{lines[i]}"
                            if "n" in flags:
                                curr = f"{i + 1}:{curr}"
                            if len(files) > 1:
                                curr = f"{filename}:{curr}"
                    else:
                        if line != pattern + "\n":
                            if "l" in flags:
                                res += f"{filename}\n"
                                break
                            curr = f"{lines[i]}"
                            if "n" in flags:
                                curr = f"{i + 1}:{curr}"
                            if len(files) > 1:
                                curr = f"{filename}:{curr}"
                res += curr
    return res
