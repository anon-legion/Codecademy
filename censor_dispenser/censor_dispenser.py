# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


def censor(email, target, nWord_target = [], frenzy = False):
    """
    
    Parameters
    ----------
    email : str
        a multi-line string which will be the subject of scanning and mutating for censoring
    target : list
        a list of words to be scanned and censored from the email
    nWord_target : list, optional
        similar to target but will only censor after 2 instances of occurence. The default is [].
    frenzy : bool, optional
        argument whether or not to use the frenzy_censor which appends the list of hits to also censor words before and after censored words from target and nWord

    Returns
    -------
    str
        Given the appropriate arguments, the function returns a mutated version of email with any occurence of words from target and nWord censored

    """
    email_list = [newline.split() for newline in email.split('\n')]
    scan_list = [[word.strip(',.!?()"').lower() for word in line] for line in email_list]
    target_list = [term.split() for term in target]
    nWord_list = [term.split() for term in nWord_target]
    hits = []
    nWord_count = 0
    
    #scanning and locating
    #step 1 iterate through every group/list (new line) in scan_list
    for line in range(len(scan_list)):
        #step 2 iterate through every element (word) in the group/list in scan_list
        for word in range(len(scan_list[line])):
            #step 3 iterate through target_list for every element in scan_list
            for y in range(len(target_list)):
                #step 4 compare elements in target_list to scan_list
                for z in range(len(target_list[y])):
                    if not word + z < len(scan_list[line]):
                        break
                    if (target_list[y][z] == scan_list[line][word + z] or target_list[y][z] + 's' == scan_list[line][word + z]) and z == len(target_list[y]) - 1:
                        #storing hits
                        hits.append([hit for hit in range(word, word + len(target_list[y]))])
                        #storing index of line/group/list where hits are located as last element
                        hits[len(hits) - 1].append(line)                        
                    elif scan_list[line][word + z] == target_list[y][z] or target_list[y][z] + 's' == scan_list[line][word + z]:
                        continue
                    else:
                        break
            #iterates through nWord_list (negative words) similar to target_list
            for a in range(len(nWord_list)):
                for b in range(len(nWord_list[a])):
                    if not word + b < len(scan_list[line]):
                        break
                    if (nWord_list[a][b] == scan_list[line][word + b] or nWord_list[a][b] + 's' == scan_list[line][word + b]) and b == len(nWord_list[a]) - 1:
                        nWord_count += 1
                        if nWord_count > 2:
                            hits.append([hit for hit in range(word, word + len(nWord_list[a]))])
                            hits[len(hits) - 1].append(line)                        
                    elif scan_list[line][word + b] == nWord_list[a][b] or nWord_list[a][b] + 's' == scan_list[line][word + b]:
                        continue
                    else:
                        break
                    
    def fenzy_censor(hits):
        """
        
        Parameters
        ----------
        hits : list
            a list of indeces where the occurence of words from target and/or nWord are

        Returns
        -------
        list
            Given the appropriate arguments, the function mutates the list of hits by appending the indeces of words before and after the words already in hits

        """
        before = []
        after = []
        for x in hits:
            if x[0] == 0 and x[-1] == 0:
                continue
            elif x[0] == 0:
                if len(scan_list[x[-1] - 1]) == 0:
                    continue
                else:
                    before.append([-1, x[-1] - 1])
            else:
                before.append([x[0] - 1, x[-1]])
        
        for x in hits:
            if x[-2] + 1 == len(scan_list[x[-1]]) and x[-1] + 1 == len(scan_list):
                break
            elif x[-2] + 1 == len(scan_list[x[-1]]):
                if len(scan_list[x[-1] + 1]) == 0:
                    continue
                else:
                    after.append([0, x[-1] + 1])
            else:
                after.append([x[-2] + 1, x[-1]])
        return (before + hits + after)
    
    # def isOut_of_range(hits):
    #     """
    #     this is a function used to check the results of frenzy_censor()

    #     Parameters
    #     ----------
    #     hits : list
    #         list of the indeces of the words to be censored

    #     Returns
    #         given the appropriate input, the function checks and returns whether or not the indeces are out of range when in a list of strings (scan_list) containing the words of the contents of an email (email_one, email_two, email_three, email_four)
    #     -------
    #     oor : list
    #         the indeces that are out of range
    #     """
    #     oor = []
    #     for hit in hits:
    #         if hit[-2] < len(scan_list[hit[-1]]):
    #             print('{} is NOT out of range! Index {} of scanlist has a length of {}'.format(hit, hit[-1], len(scan_list[hit[-1]])))
    #         else:
    #             print('{} is out of range! Index {} of scanlist only has a length of {}'.format(hit, hit[-1], len(scan_list[hit[-1]])))
    #             oor.append(hit)
    #     return oor
     
    #replacing censored words from original email using index in hits (the last element of every list in hits is the index of the group/list (line) where the target (word) is located in email_list)
    if frenzy == False:
        for hit in hits:
            for i in hit[:-1]:
                email_list[hit[-1]][i] = email_list[hit[-1]][i].lower().replace(scan_list[hit[-1]][i], '*' * len(scan_list[hit[-1]][i]))
        return('\n'.join([' '.join(lines) for lines in email_list]))
    else:
        for hit in fenzy_censor(hits):
            for i in hit[:-1]:
                email_list[hit[-1]][i] = email_list[hit[-1]][i].lower().replace(scan_list[hit[-1]][i], '*' * len(scan_list[hit[-1]][i]))
        return('\n'.join([' '.join(lines) for lines in email_list]))

print(censor(email_four, proprietary_terms, negative_words, True))