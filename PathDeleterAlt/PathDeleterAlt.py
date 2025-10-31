from autopkglib import Processor, ProcessorError
import os
import shutil

__all__ = ["PathDeleterAlt"]

class PathDeleterAlt(Processor):
    description = "Deletes files/folders from a list."
    input_variables = {
        "path_list": {
            "required": True,
            "description": "List of paths to delete"
        }
    }

    def main(self):
        for path in self.env.get("path_list", []):
            if os.path.exists(path):
                print(f"Deleting {path}")
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                except Exception as e:
                    raise ProcessorError(f"Failed to delete {path}: {e}")
            else:
                print(f"Path does not exist: {path}")
