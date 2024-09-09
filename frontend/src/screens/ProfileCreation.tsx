import React, { useState } from 'react';
import { View, TextInput, Button } from 'react-native';
import { createProfile } from '../services/profile';

const ProfileCreation = () => {
  const [name, setName] = useState('');
  const [bio, setBio] = useState('');

  const handleSubmit = async () => {
    try {
      await createProfile({ name, bio });
      // Navigate to the next screen
    } catch (error) {
      console.error('Error creating profile:', error);
    }
  };

  return (
    <View>
      <TextInput placeholder="Name" value={name} onChangeText={setName} />
      <TextInput placeholder="Bio" value={bio} onChangeText={setBio} multiline />
      <Button title="Create Profile" onPress={handleSubmit} />
    </View>
  );
};

export default ProfileCreation;