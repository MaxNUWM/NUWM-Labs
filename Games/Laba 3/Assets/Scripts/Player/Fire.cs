using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fire : MonoBehaviour
{
    private WeaponManager weaponMan;
    // Start is called before the first frame update
    void Awake()
    {
        weaponMan = GetComponent<WeaponManager>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            weaponMan.GetCur().Fire();
            
        }
        else
        {
            return;
        }
    }
}
