import re
from modules.ErrorHandling import ErrorHandling

e_h = ErrorHandling()

with open("bigcode_qwen_full.txt", "r") as f:
    data = f.read()

error_patter = r"([EF]\.?|\.?[EF])\n\=+(.*?)(?:\=+\sSTART)"
all_errors = re.findall(error_patter, data, re.DOTALL)
all_errors = ["\n".join(error[1].splitlines()[:-2]).strip() for error in all_errors]
all_errors = [e_h.remove_multithread_generic_error(error) for error in all_errors if error]



# with open("all_errors.txt", "w") as f:
#     for error in all_errors:
#         f.write(error)
#         f.write("\n")
#         f.write("#"*100)
#         f.write("\n")