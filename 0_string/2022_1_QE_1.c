#include <stdio.h>
#include <stdbool.h> //bool
#include <string.h> //char 

// 이때 char는 array라서 pointer의 형태로 넣어줘야함. 
bool is_palindrome(const char* s) {
    int len_s = strlen(s);
    int mid = len_s / 2;
    int l;
    int r;

    if (len_s % 2 == 0) {
        l = mid - 1;
        r = mid;
    } else {
        l = r = mid;
    }

    while (l > -1 && r < len_s && s[l] == s[r]) {
        l -= 1;
        r += 1;
    }

    return (l == -1) ? true : false;
}

// int main() {
//     const char* s = "mym";
//     printf("%d\n", is_palindrome(s));
//     return 0;
// }

bool substring(const char* s, const char* t) {
    int len_s = strlen(s);
    int len_t = strlen(t);

    if (len_s >= len_t) {
        int difference_len = len_s - len_t;
        for (int idx = 0; idx <= difference_len; ++idx) {
            if (strncmp(s + idx, t, len_t) == 0) {
                return true;
            }
        }
    }

    return false;
}

// int main() {
//     const char* s = "abcdef";
//     const char* t = "bcd";
//     bool result = substring(s, t);

//     if (result) {
//         printf("'%s' is a substring of '%s'\n", t, s);
//     } else {
//         printf("'%s' is not a substring of '%s'\n", t, s);
//     }

//     return 0;
// }

char** max_palindrome(const char* s, int* count) {
    int max_count = 0;
    int capacity = 10;
    char** temp = (char**)malloc(capacity * sizeof(char*));

    // Find all palindromes
    for (int i = 0; i < strlen(s); ++i) {
        for (int j = i; j <= strlen(s); ++j) {
            char* candidate_s = strndup(s + i, j - i); // strndup(src, len) 
            if (is_palindrome(candidate_s)) {
                if (max_count >= capacity) {
                    capacity *= 2;
                    temp = (char**)realloc(temp, capacity * sizeof(char*));
                }
                temp[max_count++] = candidate_s;
            } else {
                free(candidate_s);
            }
        }
    }

    char** result = (char**)malloc(max_count * sizeof(char*));
    int result_count = 0;
    for (int i = 0; i < max_count; ++i) {
        if (strlen(temp[i]) > 0) {
            result[result_count++] = temp[i];
        } else {
            free(temp[i]);
        }
    }
    free(temp);

    // Remove redundant substrings
    for (int i = 0; i < result_count - 1; ++i) {
        for (int j = i + 1; j < result_count; ++j) {
            if (substring(result[i], result[j])) {
                free(result[j]);
                result[j] = NULL;
            } else if (substring(result[j], result[i])) {
                free(result[i]);
                result[i] = NULL;
                break;
            }
        }
    }

    char** ans = (char**)malloc(result_count * sizeof(char*));
    int ans_count = 0;
    for (int i = 0; i < result_count; ++i) {
        if (result[i] != NULL) {
            ans[ans_count++] = result[i];
        }
    }
    free(result);

    *count = ans_count;
    return ans;
}

int main() {
    const char* s = "babad";
    int count;
    char** result = max_palindrome(s, &count);

    for (int i = 0; i < count; ++i) {
        printf("%s ", result[i]);
        free(result[i]);
    }
    free(result);

    return 0;
}
