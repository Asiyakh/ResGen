import {Typography, Button, Grid} from '@mui/material'
import { useState } from 'react'
import raw from "./Output/MMbulletPoints.txt"

function App() {

  const [MMBullet, getMMBullet] = useState(null)
  const [HMMBullet, getHMMBullet] = useState(null)
  const [HFBullet, getHFBullet] = useState(null)



  function readTextFile(file){
    fetch(file)
    .then(r => r.text())
    .then(text => getMMBullet(text.split('\n')[Math.floor((Math.random() * 500) + 1)]));
  }

  const unHideMM = () => { 
    getMMBullet(readTextFile(raw))
  }

  const unHideHMM = () => {
    getHMMBullet("insert bulletpoint")
  }

  const unHideHF = () => {
    getHFBullet("insert bulletpoint")
  }

  return (
    <Grid container direction="column"
    justifyContent="center"
    alignItems="center"
    style = {{height:"100vh"}}
    padding='50px'
    className="App">
      <Typography variant="h1"> ResGen </Typography>
      <Typography variant="s2" marginTop='30px'> Click a button below for a resume bulletpoint! </Typography>

      <div style={{marginTop: '20px', marginBottom: '20px'}}>
      <Button variant="contained" onClick={unHideMM} sx={{marginRight: '5px'}}>Markov Model Algorithm</Button>
      <Button variant="contained" onClick={unHideHMM} sx={{marginRight: '5px'}}>Hidden Markov Model Algorithm</Button>
      <Button variant="outlined" sx={{marginRight: '5px'}}onClick={unHideHF}>Transformer Algorithm</Button>
      </div >

      {!!MMBullet && <Typography> <Typography display='inline' fontWeight={800}> Markov Model: </Typography> {MMBullet}</Typography>}

      {!!HMMBullet && <Typography><Typography display='inline' fontWeight={800}> Hidden Markov Model: </Typography> {HMMBullet}</Typography>}

      {!!HFBullet && <Typography><Typography display='inline' fontWeight={800}> Transformer Model: </Typography> {HFBullet}</Typography>}
    </Grid>
  );
}

export default App;
