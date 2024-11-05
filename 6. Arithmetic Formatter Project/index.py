def arithmetic_arranger(problems, show_answers=False):
    outputs = []
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    else:
        for problem in problems:
            parts = problem.split()
        
            if parts[1] not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
            if not parts[0].isdigit() or not parts[2].isdigit():
                return 'Error: Numbers must only contain digits.'
            if len(parts[0]) > 4 or len(parts[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            elif '+' in problem:
                first_int = problem.split(' ')[0]
                second_int = problem.split(' ')[2]
                result = int(first_int) + int(second_int)
                result = str(result)
                if len(first_int) >= len(second_int) and len(first_int) >= len(result):
                    len_first_int = len(first_int)
                    dash_first_length = len_first_int + 2
                    outputs.append((first_int.rjust(dash_first_length) + '\n' + '+ ' + second_int.rjust(len_first_int) + '\n' + '-' * dash_first_length + '\n' + result.rjust(dash_first_length)))
                elif len(first_int) <= len(second_int) and len(second_int) >= len(result):
                    len_second_int = len(second_int)
                    dash_second_length = len_second_int + 2
                    outputs.append((first_int.rjust(dash_second_length) + '\n' + '+ ' + second_int.rjust(len_second_int) + '\n' + '-' * dash_second_length + '\n' + result.rjust(dash_second_length)))
                elif len(result) > len(first_int) or len(result) > len(second_int):
                    if len(result) > len(first_int):
                        len_result = len(result)
                        dash_result_length = len_result + 1
                        outputs.append((first_int.rjust(dash_result_length) + '\n' + '+' + second_int.rjust(len_result) + '\n' + '-' * dash_result_length + '\n' + result.rjust(dash_result_length)))
                    else:
                        len_result = len(result)
                        dash_result_length = len_result + 1
                        outputs.append(first_int.rjust(dash_result_length) + '\n' + '+' + second_int.rjust(len_result) + '\n' + '-' * dash_result_length + '\n' + result.rjust(dash_result_length))
            elif '-' in problem:
                first_int_neg = problem.split(' ')[0]
                second_int_neg = problem.split(' ')[2]
                result_neg = int(first_int_neg) - int(second_int_neg)
                result_neg = str(result_neg)
                if len(first_int_neg) >= len(second_int_neg) and len(first_int_neg) >= len(result_neg):
                    len_first_int_neg = len(first_int_neg)
                    dash_first_length_neg = len_first_int_neg + 2
                    outputs.append((first_int_neg.rjust(dash_first_length_neg) + '\n' + '- ' + second_int_neg.rjust(len_first_int_neg) + '\n' + '-' * dash_first_length_neg + '\n' + result_neg.rjust(dash_first_length_neg)))
                elif len(first_int_neg) <= len(second_int_neg) and len(second_int_neg) >= len(result_neg):
                    len_second_int_neg = len(second_int_neg)
                    dash_second_length_neg = len_second_int_neg + 2
                    outputs.append((first_int_neg.rjust(dash_second_length_neg) + '\n' + '- ' + second_int_neg.rjust(len_second_int_neg) + '\n' + '-' * dash_second_length_neg + '\n' + result_neg.rjust(dash_second_length_neg)))
                elif len(result_neg) > len(first_int_neg) or len(result_neg) > len(second_int_neg):
                    if len(result_neg) > len(first_int_neg):
                        len_result_neg = len(result_neg)
                        dash_result_length_neg = len_result_neg + 1
                        outputs.append((first_int_neg.rjust(dash_result_length_neg) + '\n' + '-' + second_int_neg.rjust(len_result_neg) + '\n' + '-' * dash_result_length_neg + '\n' + result_neg.rjust(dash_result_length_neg)))
                    else:
                        len_result_neg = len(result_neg)
                        dash_result_length_neg = len_result_neg + 1
                        outputs.append(first_int_neg.rjust(dash_result_length_neg) + '\n' + '-' + second_int_neg.rjust(len_result_neg) + '\n' + '-' * dash_result_length_neg + '\n' + result_neg.rjust(dash_result_length_neg))
                            
        split_items = [output.split('\n') for output in outputs]
        max_lines = max(len(item) for item in split_items)
        arranged_lines = []

        if show_answers == False:
            for i in range(max_lines - 1):
                line = []
                for item in split_items:
                    if i < len(item):
                        line.append(item[i].ljust(len(item[0])))
                    else:
                        line.append(' ' * len(item[0]))
                arranged_lines.append('    '.join(line))
        elif show_answers == True:
            for i in range(max_lines):
                line = []
                for item in split_items:
                    if i < len(item):
                        line.append(item[i].ljust(len(item[0])))
                    else:
                        line.append(' ' * len(item[0]))
                arranged_lines.append('    '.join(line))

        return '\n'.join(arranged_lines)

solution = arithmetic_arranger(["3 + 855", "988 + 40"], True)
print(solution)
