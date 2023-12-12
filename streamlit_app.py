import streamlit as st
import json

st.title('Capture IG Unfollowers')

st.warning("Followers")
followers = st.file_uploader("Upload Followers File", type=["json"])
st.write("\n")
st.warning("Following")
following = st.file_uploader("Upload Following File", type=["json"])


# getting followers
if followers is not None:
  followers1 = followers.read().decode('utf-8')
  json_data1 = json.loads(followers1)


# getting following
if following is not None:
  following1 = following.read().decode('utf-8')
  json_data2 = json.loads(following1)



if st.button('Capture'):

  followers2 = [item['string_list_data'][0]['value'] for item in json_data1]
  following2 = [item1['string_list_data'][0]['value'] for item1 in json_data2['relationships_following']]
  
  unfollowers = list(set(following2) - set(followers2))
  sorted_ls = sorted(unfollowers)
  
  
  st.error("\nNo of Unfollowers: " + str(len(unfollowers)) + "\n")
  st.write('\n')
  st.write(sorted_ls)
