from agents import function_tool
import httpx
from config import logger

def validate_pr_url(pr_url: str) -> bool:
    # https://github.com/pythoncpp/test-code/pull/1
    # split the url in parts on /
    parts = pr_url.split("/")

    # check if all the components are available in url
    if len(parts) !=7 or parts[5] not in ['pulll', 'pulls']:
        raise Exception("invalid pr url detected.")

    #extract the components from the url
    owner = parts[3]
    repo = parts[4]
    pr_number = parts[6]

    return owner, repo, pr_number

@function_tool
def fetch_pull_request_diff(pr_url: str):
    """
    Description: This tool is used to fetch pull request diff.
    Args:
        pr_url: url of pr whose diff is needed.
    Returns: consolidated diff from the pr.
    """

    owner, repo, pr_number = validate_pr_url(pr_url=pr_url)
    logger.info(f"owner: {owner}, repo: {repo}, pr_number : {pr_number}")

    # build the url to download files from the repo
    file_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    # fetch all the files from the pr
    reponse = httpx.get(file_url)

    if reponse.status_code == 200:
        # get the files from the pr
        files = reponse.json()
        if not files:
            raise Exception(f"the pr {pr_number} does not have files")

        # collect all the diff
        diffs = []
        for file in files:
            # extract the diff metadata
            filename = file.get("filename")
            patch = file.get("patch")
            deletions = file.get("deletions")
            additions = file.get("additions")
            status = file.get("status")

            diff_header = f"--{filename} ({status}, +{additions}/-{deletions}) --"
            diffs.append(f"{diff_header}\n{patch}")

        return "\n\n".join(diffs)
    else:
        raise Exception("error while loading files from the PR")




