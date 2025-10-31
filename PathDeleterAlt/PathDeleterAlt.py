from autopkglib import Processor, ProcessorError
import os
import shutil

__all__ = ["PathDeleterAlt"]

class PathDeleterAlt(Processor):
    description = "Deletes a file or folder."
    input_variables = {
        "RECREATE_PATH": {
            "default": True,
            "required": False,
            "description": (
                "Recreate the path if deleted."
            ),
        },
        "PATH": {
            "required": True,
            "description": "path to delete"
        }
    }

    output_variables = {
        "pathdeleteralt_summary_result": {
            "description": "PathDeleteAlt report data."
        },
    }

    def main(self):
        path = self.env.get("PATH", None)
        if path:
            if os.path.exists(path):
                self.output(f"Deleting {path}")
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    if self.env.get("RECREATE_PATH"):
                        self.output(f"Recreating {path}")
                        os.mkdir(path)
                except Exception as e:
                    raise ProcessorError(f"Failed to delete {path}: {e}")
            else:
                self.output(f"Path does not exist: {path}")


if __name__ == "__main__":
    PROCESSOR = PathDeleterAlt()
    PROCESSOR.execute_shell()
