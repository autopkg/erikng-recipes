from autopkglib import Processor, ProcessorError
import os
import shutil

__all__ = ["PathDeleter"]

class PathDeleter(Processor):
    description = "Deletes files/folders from a list."
    input_variables = {
        "PATH": {
            "required": True,
            "description": "List of paths to delete"
        }
    }

    output_variables = {
        "pathdeleter_summary_result": {
            "description": "PathDeleter report data."
        },
    }

    def main(self):
        path = self.env.get("PATH", None)
        if path:
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


if __name__ == "__main__":
    PROCESSOR = PathDeleter()
    PROCESSOR.execute_shell()
