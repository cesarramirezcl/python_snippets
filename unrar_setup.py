import os
from google.cloud import storage
import rarfile
import tempfile

class UnrarSetup:
  """
  A utility class to set up and use an 'unrar' binary from Google Cloud Storage (GCS).

  This class is designed to download and set up the 'unrar' binary for the `rarfile` library from a provided GCS path.
  The binary is downloaded to a temporary directory and made executable.

  Attributes:
  -----------
  gcs_bucket : str
    The name of the GCS bucket where the 'unrar' binary is stored.
  unrar_blob_name : str
    The path to the 'unrar' binary within the GCS bucket.
  temp_dir : str
    The path to the temporary directory where the 'unrar' binary will be downloaded.

  Methods:
  --------
  _parse_gcs_path(gcs_path: str) -> Tuple[str, str]:
    Parses a GCS path to extract and return the bucket name and blob name.
  _download_from_gcs(bucket_name: str, blob_name: str, destination_file_name: str) -> None:
    Downloads a file from GCS to a specified destination.
  setup_unrar() -> None:
    Sets up the 'unrar' binary by downloading it from GCS, making it executable,
    and setting its path for the `rarfile` library.

  Example:
  --------
  unrar_setup = UnrarSetup("gs://my-bucket/path/to/unrar")
  """


  def __init__(self, gcs_unrar_path):
    """
    Initializes the UnrarSetup instance with a GCS path to the 'unrar' binary.

    Parameters:
    -----------
    gcs_unrar_path : str
      The GCS path to the 'unrar' binary. Must start with "gs://".
    """
    self.gcs_bucket, self.unrar_blob_name = self._parse_gcs_path(gcs_unrar_path)
    self.temp_dir = tempfile.gettempdir()
    self.setup_unrar()


  def _parse_gcs_path(self, gcs_path):
    """
    Parses a GCS path to extract and return the bucket name and blob name.

    Parameters:
    -----------
    gcs_path : str
        The GCS path to parse. Must start with "gs://".

    Returns:
    --------
    Tuple[str, str]
        A tuple containing the bucket name and blob name.

    Raises:
    -------
    ValueError:
        If the provided path doesn't start with "gs://".
    """
    # Extract bucket and blob name from GCS path
    if not gcs_path.startswith("gs://"):
      raise ValueError("Not a valid GCS path")
    parts = gcs_path[5:].split("/")
    bucket = parts[0]
    blob_name = "/".join(parts[1:])
    return bucket, blob_name


  def _download_from_gcs(self, bucket_name, blob_name, destination_file_name):
    """
    Downloads a file from GCS to a specified destination.

    Parameters:
    -----------
    bucket_name : str
        The name of the GCS bucket.
    blob_name : str
        The name of the blob (file) to download.
    destination_file_name : str
        The local path where the file should be saved.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(destination_file_name)

  def setup_unrar(self):
    """
    Sets up the 'unrar' binary by downloading it from GCS, making it executable,
    and setting its path for the `rarfile` library.
    """
    unrar_path = os.path.join(self.temp_dir, "unrar")

    # Download unrar binary to the temp directory
    self._download_from_gcs(self.gcs_bucket, self.unrar_blob_name, unrar_path)

    # Ensure the binary is executable
    os.chmod(unrar_path, 0o755)

    # Set the path to the unrar tool for the rarfile library
    rarfile.UNRAR_TOOL = unrar_path
