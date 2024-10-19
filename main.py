import os
import shutil
import subprocess
from gradio_client import Client, handle_file
import gradio
import sys
import requests
import time

trigger_word = ""
LoRA_name = "test" #Enter the name of your LoRA 


script_path = os.path.abspath("ai-toolkit/flux_train_ui.py")
script_dir = os.path.dirname(script_path)

# Change the current working directory to the script's directory
os.chdir(script_dir)

# Change the current working directory to the script's directory

process = subprocess.Popen(
    [sys.executable, "flux_train_ui.py"],
    cwd=script_dir  # Set the working directory for the subprocess
)

current_directory = os.getcwd()
print(f'Initial----> {current_directory}')

gradio_url = "http://127.0.0.1:7860/"
while True:
    try:
        response = requests.get(gradio_url)
        if response.status_code == 200:
            print("Gradio app is ready")
            break
    except requests.ConnectionError:
        pass
    time.sleep(1)  # Wait for 1 second before checking again

time.sleep(10)

print("AI-Toolkit - Gradio UI launched successfully")


def get_image_file_paths(directory):
    image_extensions = ('.png', '.jpg', '.jpeg')
    image_paths = [os.path.abspath(os.path.join(directory, f)) for f in os.listdir(directory) if f.lower().endswith(image_extensions)]
    print(image_paths)
    return image_paths

current_directory = os.path.join("..","Upload_Images")
image_paths = get_image_file_paths(current_directory)


client = Client("http://127.0.0.1:7860/")
result = client.predict(
        uploaded_files=[handle_file(path) for path in image_paths],
		concept_sentence="Hello!!",
		api_name="/load_captioning"
)
#print(result)

current_directory = os.getcwd()
print(f'Inside----> {current_directory}')

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		images=[handle_file(path) for path in image_paths],
        concept_sentence=trigger_word,
		param_2="Hello!!",
		param_3="Hello!!",
		param_4="Hello!!",
		param_5="Hello!!",
		param_6="Hello!!",
		param_7="Hello!!",
		param_8="Hello!!",
		param_9="Hello!!",
		param_10="Hello!!",
		param_11="Hello!!",
		param_12="Hello!!",
		param_13="Hello!!",
		param_14="Hello!!",
		param_15="Hello!!",
		param_16="Hello!!",
		param_17="Hello!!",
		param_18="Hello!!",
		param_19="Hello!!",
		param_20="Hello!!",
		param_21="Hello!!",
		param_22="Hello!!",
		param_23="Hello!!",
		param_24="Hello!!",
		param_25="Hello!!",
		param_26="Hello!!",
		param_27="Hello!!",
		param_28="Hello!!",
		param_29="Hello!!",
		param_30="Hello!!",
		param_31="Hello!!",
		param_32="Hello!!",
		param_33="Hello!!",
		param_34="Hello!!",
		param_35="Hello!!",
		param_36="Hello!!",
		param_37="Hello!!",
		param_38="Hello!!",
		param_39="Hello!!",
		param_40="Hello!!",
		param_41="Hello!!",
		param_42="Hello!!",
		param_43="Hello!!",
		param_44="Hello!!",
		param_45="Hello!!",
		param_46="Hello!!",
		param_47="Hello!!",
		param_48="Hello!!",
		param_49="Hello!!",
		param_50="Hello!!",
		param_51="Hello!!",
		param_52="Hello!!",
		param_53="Hello!!",
		param_54="Hello!!",
		param_55="Hello!!",
		param_56="Hello!!",
		param_57="Hello!!",
		param_58="Hello!!",
		param_59="Hello!!",
		param_60="Hello!!",
		param_61="Hello!!",
		param_62="Hello!!",
		param_63="Hello!!",
		param_64="Hello!!",
		param_65="Hello!!",
		param_66="Hello!!",
		param_67="Hello!!",
		param_68="Hello!!",
		param_69="Hello!!",
		param_70="Hello!!",
		param_71="Hello!!",
		param_72="Hello!!",
		param_73="Hello!!",
		param_74="Hello!!",
		param_75="Hello!!",
		param_76="Hello!!",
		param_77="Hello!!",
		param_78="Hello!!",
		param_79="Hello!!",
		param_80="Hello!!",
		param_81="Hello!!",
		param_82="Hello!!",
		param_83="Hello!!",
		param_84="Hello!!",
		param_85="Hello!!",
		param_86="Hello!!",
		param_87="Hello!!",
		param_88="Hello!!",
		param_89="Hello!!",
		param_90="Hello!!",
		param_91="Hello!!",
		param_92="Hello!!",
		param_93="Hello!!",
		param_94="Hello!!",
		param_95="Hello!!",
		param_96="Hello!!",
		param_97="Hello!!",
		param_98="Hello!!",
		param_99="Hello!!",
		param_100="Hello!!",
		param_101="Hello!!",
		param_102="Hello!!",
		param_103="Hello!!",
		param_104="Hello!!",
		param_105="Hello!!",
		param_106="Hello!!",
		param_107="Hello!!",
		param_108="Hello!!",
		param_109="Hello!!",
		param_110="Hello!!",
		param_111="Hello!!",
		param_112="Hello!!",
		param_113="Hello!!",
		param_114="Hello!!",
		param_115="Hello!!",
		param_116="Hello!!",
		param_117="Hello!!",
		param_118="Hello!!",
		param_119="Hello!!",
		param_120="Hello!!",
		param_121="Hello!!",
		param_122="Hello!!",
		param_123="Hello!!",
		param_124="Hello!!",
		param_125="Hello!!",
		param_126="Hello!!",
		param_127="Hello!!",
		param_128="Hello!!",
		param_129="Hello!!",
		param_130="Hello!!",
		param_131="Hello!!",
		param_132="Hello!!",
		param_133="Hello!!",
		param_134="Hello!!",
		param_135="Hello!!",
		param_136="Hello!!",
		param_137="Hello!!",
		param_138="Hello!!",
		param_139="Hello!!",
		param_140="Hello!!",
		param_141="Hello!!",
		param_142="Hello!!",
		param_143="Hello!!",
		param_144="Hello!!",
		param_145="Hello!!",
		param_146="Hello!!",
		param_147="Hello!!",
		param_148="Hello!!",
		param_149="Hello!!",
		param_150="Hello!!",
		param_151="Hello!!",
		api_name="/Do Captioning"
)
#print(result)


client = Client("http://127.0.0.1:7860/")
result = client.predict(
    lora_name=LoRA_name,
    concept_sentence=trigger_word,
    sample_1="",
	sample_2="",
	sample_3="",
	param_13=[handle_file(path) for path in image_paths],
	param_14="Hello!!",
	param_15="Hello!!",
	param_16="Hello!!",
	param_17="Hello!!",
	param_18="Hello!!",
	param_19="Hello!!",
	param_20="Hello!!",
	param_21="Hello!!",
	param_22="Hello!!",
	param_23="Hello!!",
	param_24="Hello!!",
	param_25="Hello!!",
	param_26="Hello!!",
	param_27="Hello!!",
	param_28="Hello!!",
	param_29="Hello!!",
	param_30="Hello!!",
	param_31="Hello!!",
	param_32="Hello!!",
	param_33="Hello!!",
	param_34="Hello!!",
	param_35="Hello!!",
	param_36="Hello!!",
	param_37="Hello!!",
	param_38="Hello!!",
	param_39="Hello!!",
	param_40="Hello!!",
	param_41="Hello!!",
	param_42="Hello!!",
	param_43="Hello!!",
	param_44="Hello!!",
	param_45="Hello!!",
	param_46="Hello!!",
	param_47="Hello!!",
	param_48="Hello!!",
	param_49="Hello!!",
	param_50="Hello!!",
	param_51="Hello!!",
	param_52="Hello!!",
	param_53="Hello!!",
	param_54="Hello!!",
	param_55="Hello!!",
	param_56="Hello!!",
	param_57="Hello!!",
	param_58="Hello!!",
	param_59="Hello!!",
	param_60="Hello!!",
	param_61="Hello!!",
	param_62="Hello!!",
	param_63="Hello!!",
	param_64="Hello!!",
	param_65="Hello!!",
	param_66="Hello!!",
	param_67="Hello!!",
	param_68="Hello!!",
	param_69="Hello!!",
	param_70="Hello!!",
	param_71="Hello!!",
	param_72="Hello!!",
	param_73="Hello!!",
	param_74="Hello!!",
	param_75="Hello!!",
	param_76="Hello!!",
	param_77="Hello!!",
	param_78="Hello!!",
	param_79="Hello!!",
	param_80="Hello!!",
	param_81="Hello!!",
	param_82="Hello!!",
	param_83="Hello!!",
	param_84="Hello!!",
	param_85="Hello!!",
	param_86="Hello!!",
	param_87="Hello!!",
	param_88="Hello!!",
	param_89="Hello!!",
	param_90="Hello!!",
	param_91="Hello!!",
	param_92="Hello!!",
	param_93="Hello!!",
	param_94="Hello!!",
	param_95="Hello!!",
	param_96="Hello!!",
	param_97="Hello!!",
	param_98="Hello!!",
	param_99="Hello!!",
	param_100="Hello!!",
	param_101="Hello!!",
	param_102="Hello!!",
	param_103="Hello!!",
	param_104="Hello!!",
	param_105="Hello!!",
	param_106="Hello!!",
	param_107="Hello!!",
	param_108="Hello!!",
	param_109="Hello!!",
	param_110="Hello!!",
	param_111="Hello!!",
	param_112="Hello!!",
	param_113="Hello!!",
	param_114="Hello!!",
	param_115="Hello!!",
	param_116="Hello!!",
	param_117="Hello!!",
	param_118="Hello!!",
	param_119="Hello!!",
	param_120="Hello!!",
	param_121="Hello!!",
	param_122="Hello!!",
	param_123="Hello!!",
	param_124="Hello!!",
	param_125="Hello!!",
	param_126="Hello!!",
	param_127="Hello!!",
	param_128="Hello!!",
	param_129="Hello!!",
	param_130="Hello!!",
	param_131="Hello!!",
	param_132="Hello!!",
	param_133="Hello!!",
	param_134="Hello!!",
	param_135="Hello!!",
	param_136="Hello!!",
	param_137="Hello!!",
	param_138="Hello!!",
	param_139="Hello!!",
	param_140="Hello!!",
	param_141="Hello!!",
	param_142="Hello!!",
	param_143="Hello!!",
	param_144="Hello!!",
	param_145="Hello!!",
	param_146="Hello!!",
	param_147="Hello!!",
	param_148="Hello!!",
	param_149="Hello!!",
	param_150="Hello!!",
	param_151="Hello!!",
	param_152="Hello!!",
	param_153="Hello!!",
	param_154="Hello!!",
	param_155="Hello!!",
	param_156="Hello!!",
	param_157="Hello!!",
	param_158="Hello!!",
	param_159="Hello!!",
	param_160="Hello!!",
	param_161="Hello!!",
	param_162="Hello!!",
	param_163="Hello!!",
	api_name="/start_training"
)
print(result)

def format_lora_name(lora_name):
    # Convert to lowercase
    formatted_name = lora_name.lower()
    # Replace spaces with hyphens
    formatted_name = formatted_name.replace(" ", "-")
    return formatted_name


formatted_name = format_lora_name(LoRA_name)
#print(formatted_name)  


source_folder = os.path.join("output", formatted_name, f"{formatted_name}.safetensors")
destination_folder = os.path.join("outputs", LoRA_name)

if os.path.exists(source_folder):
    os.makedirs(destination_folder, exist_ok=True) 
    shutil.copy2(source_folder, destination_folder)
    print(f"Contents of {source_folder} copied to {destination_folder}")
else :
    print("Does not exist")