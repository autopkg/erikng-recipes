#!/usr/bin/python

import json

from autopkglib import Processor, ProcessorError, URLGetter

__all__ = ["GenymotionURLProvider"]


class GenymotionURLProvider(URLGetter):
    """Processor class."""

    decription = "Uses Genymotion API to find the latest version of application."
    input_variables = {}
    output_variables = {"genymotion_version": {"description": "Version number",}}

    description = __doc__

    def get_version(self):
        """Get version from Genymotion API."""

        # Genymotion Update API
        url = "https://cloud.genymotion.com/launchpad/last_version/mac/x64/"
        # API requires AJAX / XMLHttpRequest
        headers = {"X-Requested-With": "XMLHttpRequest", "User-Agent": "Safari"}
        try:
            response = self.download(url, headers=headers)
            # Convert response to JSON
            jsondata = json.loads(response)
            # Example json return: {u'url': u'http://files2.genymotion.com/genymotion/genymotion-2.7.2/genymotion-2.7.2.dmg', u'version': u'2.7.2'}
            return jsondata["version"]
        except:
            raise ProcessorError("Could not retrieve version from URL: %s" % url)

    def main(self):
        """Main process."""

        self.env["genymotion_version"] = self.get_version()
        self.output("Version: %s" % self.env["genymotion_version"])


if __name__ == "__main__":
    PROCESSOR = GenymotionURLProvider()
    PROCESSOR.execute_shell()
