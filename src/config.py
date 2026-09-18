from dotenv import load_dotenv
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# load the environment variables
load_dotenv()

# get the configuration parameters
REVIEWER_MODEL = os.getenv("REVIEWER_MODEL", "")
CRITIC_MODEL = os.getenv("CRITIC_MODEL", "")
BASE_URL = os.getenv("BASE_URL", "")
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", ""))