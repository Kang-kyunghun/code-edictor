import json
import uuid
import subprocess

from django.http            import JsonResponse
from django.views           import View

def excute_code(language, file_path):
    interpreter = {
        "python" : "python",
        "javascript" : "node"
    }
    
    command = f"{interpreter[language]} {file_path}"
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    
    output, error = popen.communicate()
    return {
        "output" : output,
        "error"  : error
    }
    
def remove_temp_file(file_path):
    command = f"rm {file_path}"
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    
    output, error = popen.communicate()
    print(output, error)

class EditorView(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        language = data["language"]

        languages = {
            "python"     : "py",
            "javascript" : "js"
        }

        file_path = f"temp/{str(uuid.uuid4())}.{languages[language]}"
        
        with open(file_path, 'w') as f:
            f.write(data['code'])
        
        resulte = excute_code(language, file_path)
        
        if resulte['error']:
            print(file_path)
            remove_temp_file(file_path)
            return JsonResponse({"message" : resulte['error']}, status=200)
        print(file_path)
        remove_temp_file(file_path)
        return JsonResponse({"message" : resulte['output']}, status=200)