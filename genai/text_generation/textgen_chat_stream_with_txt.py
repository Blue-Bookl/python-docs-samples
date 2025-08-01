# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def generate_content() -> bool:
    # [START googlegenaisdk_textgen_chat_stream_with_txt]
    from google import genai
    from google.genai.types import HttpOptions

    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    chat_session = client.chats.create(model="gemini-2.5-flash")

    for chunk in chat_session.send_message_stream("Why is the sky blue?"):
        print(chunk.text, end="")
    # Example response:
    # The
    #  sky appears blue due to a phenomenon called **Rayleigh scattering**. Here's
    #  a breakdown of why:
    # ...
    # [END googlegenaisdk_textgen_chat_stream_with_txt]
    return True


if __name__ == "__main__":
    generate_content()
