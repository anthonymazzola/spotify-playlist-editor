
// This is just to test data when the server is down
/* import testData from '../Assets/test_playlist.json';

const getTestData = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(testData);
    }, 1000); // Simulate a delay in fetching data
  });
};

export { getTestData };
 */
export async function getTestData(endpoint, token, playlistUrl) {
  const url = `https://flask-server-ukjqkf-ca.proudsky-ad736f5d.eastus2.azurecontainerapps.io/${endpoint}?url=${playlistUrl}&token=${token}`;
  //const url = 'https://flask-server-ukjqkf-ca.proudsky-ad736f5d.eastus2.azurecontainerapps.io/${endpoint}?token=${token}';
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error('Network response problem');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}
