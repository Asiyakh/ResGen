import {Typography, Button, Grid, TextField} from '@mui/material'
import React, { useState, useEffect } from 'react'
import mm from "./Output/MMbulletPoints.txt"
import hmm from "./Output/HMMbulletPoints.txt"


function App() {


// Allows you to set port in the project properties.


  const [MMBullet, getMMBullet] = useState(null)
  const [HMMBullet, getHMMBullet] = useState(null)
  const [HFBullet, getHFBullet] = useState(null)
  const [seed, setSeed] = useState(null)
  const [data, setData] = useState([{}])

function GetMMData(){
  fetch('/mm',{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: seed
    })
  }).then(
      res => res.json()
    ).then(
      data => {
        getMMBullet(data.content)
        console.log(data)
      }
    ).catch(function(error) {
      console.log("Request failed", error);
    })
    return data.content
}

function GetHMMData(){
  fetch('/hmm',{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: seed
    })
  }).then(
      res => res.json()
    ).then(
      data => {
        getHMMBullet(data.content)
        console.log(data)
      }
    ).catch(function(error) {
      console.log("Request failed", error);
    })
    return data.content
}

function GetHFData(){
  if (!MMBullet){
  getMMBullet(GetMMData)
  }
  fetch('/hf',{
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: MMBullet
    })
  }).then(
      res => res.json()
    ).then(
      data => {
        getHFBullet(data.content)
        console.log(data)
      }
    ).catch(function(error) {
      console.log("Request failed", error);
    })
    return data.content
}

  const handleSeedChange = event => {
    setSeed(event.target.value);
  }

  const unHideHMM = () => {
    getHMMBullet(GetHMMData)
  }

  const getSeed = () => {
    return seed
  }

  const unHideHF = () => {
    getHFBullet(GetHFData())
  }

  function unHideMM() { 
    getMMBullet(GetMMData())
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
      <TextField style={{marginTop: '20px'}} id="outlined-basic" label="Start bulletpoint with" variant="outlined" size="small" onChange={handleSeedChange}/>

      <div style={{marginTop: '20px', marginBottom: '20px'}}>
      <Button variant="contained" onClick={unHideMM} sx={{marginRight: '5px'}}>Markov Model Algorithm</Button>
      <Button variant="contained" onClick={unHideHMM} sx={{marginRight: '5px'}}>Hidden Markov Model Algorithm</Button>
      <Button variant="contained" sx={{marginRight: '5px'}}onClick={unHideHF}>Transformer Algorithm</Button>
      </div >

      {!!MMBullet && <Typography> <Typography display='inline' fontWeight={800}> Markov Model: </Typography> {MMBullet}</Typography>}

      {!!HMMBullet && <Typography><Typography display='inline' fontWeight={800}> Hidden Markov Model: </Typography> {HMMBullet}</Typography>}

      {!!HFBullet && <Typography><Typography display='inline' fontWeight={800}> Transformer Model: </Typography> {HFBullet}</Typography>}
    </Grid>
  );
}

export default App;
