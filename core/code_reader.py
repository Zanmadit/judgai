import base64

def read_files(repo, paths):
    result = {}
    for p in paths:
        try:
            f = repo.get_contents(p)
            result[p] = base64.b64decode(f.content).decode("utf-8")
        except:
            result[p] = "ERROR: could not read"
    return result
