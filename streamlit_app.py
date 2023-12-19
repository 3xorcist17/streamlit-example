import streamlit as st

st.title('Capture IG Unfollowers')


st.warning("Followers")
followers = st.file_uploader("Upload Followers File", type=["json"])
st.write("\n")
st.warning("Following")
following = st.file_uploader("Upload Following File", type=["json"])
st.write("\n")
st.warning("Ignored Unfollowers")
ignore = st.file_uploader("Upload Ignored Unfollowers text file, if not upload an empty txt file", type=["txt"])

import json

# getting followers
if followers is not None:
    followers1 = followers.read().decode('utf-8')
    json_data1 = json.loads(followers1)


# getting following
if following is not None:
    following1 = following.read().decode('utf-8')
    json_data2 = json.loads(following1)


# getting ignored ones
if ignore is not None:
    ignore1 = ignore.read().decode('utf-8')

#print(ignore1)    

if st.button('Capture'):

    ignore_list = ignore1.splitlines()

    followers2 = [item['string_list_data'][0]['value'] for item in json_data1]
    following2 = [item1['string_list_data'][0]['value'] for item1 in json_data2['relationships_following']]


    unfollowers = list(set(following2) - set(followers2))
    sorted_ls = sorted(unfollowers)
    fin_ls = list(set(sorted_ls) - set(ignore_list))


    st.error("\nAll no of Unfollowers: " + str(len(unfollowers)) + "\n")
    st.warning("\nIgnored Unfollowers: " + str(len(ignore_list)) + "\n")
    st.write('\n')
    st.text('Remaining Unfollowers: ' + str(len(unfollowers)-len(ignore_list)))
    st.write(sorted(fin_ls))
    st.text('Ignored Unfollowers')
    st.write(sorted(ignore_list))


st.text('Created by SD')
